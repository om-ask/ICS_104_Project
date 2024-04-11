from enum import Enum

from searchInternal import levenshtein_automaton


class Codes(Enum):
    SUCCESS = 0
    INCONCLUSIVE = 1
    BACK = -1
    NO_RETURN = 2


class StudentRecord:

    def __init__(self, student_id: int, student_name: str, student_gpa: float):
        self._id: int = student_id
        self._name: str = student_name
        self._gpa: float = student_gpa
        self._raw: dict[str, ...] = {"ID": self._id, "Name": self._name, "GPA": self._gpa}

    def id(self) -> int:
        return self._id

    def name(self) -> str:
        return self._name

    def gpa(self) -> float:
        return self._gpa

    def raw(self) -> dict:
        return self._raw

    def modify_gpa(self, new_gpa: float):
        self._gpa = new_gpa
        self._raw["GPA"] = new_gpa

    @staticmethod
    def valid_gpa_check(response: str) -> tuple[bool, str]:
        try:
            student_gpa = float(response)

        except ValueError:
            return False, "The GPA should be a number between 0 and 4"

        if 0 <= student_gpa <= 4:
            return True, ""
        else:
            return False, "The GPA should be a number between 0 and 4"

    @staticmethod
    def valid_name_check(response: str) -> tuple[bool, str]:
        if len(response.split()) >= 2:
            return True, ""
        else:
            return False, "Please enter at least a first and second name."


class RecordsTable:

    def __init__(self, records_list=None):
        self._ids: set[int] = set()
        self._names: set[str] = set()
        self._records: list[StudentRecord] = []
        self._raw_records: list[dict[str, ...]] = []
        self._id_records: dict[int, StudentRecord] = {}
        self._name_records: dict[str, StudentRecord] = {}
        self._inverse_index: dict[str, list[tuple]] = {}
        if records_list is not None:
            for record in records_list:
                self.add_record(record)

    def records(self) -> list[StudentRecord]:
        return self._records

    def names(self) -> set[str]:
        return self._names

    def ids(self) -> set[int]:
        return self._ids

    def raw(self) -> list[dict[str, ...]]:
        return self._raw_records

    def get_record(self, student_id=None, student_name=None) -> StudentRecord:
        try:
            if student_id is not None:
                return self._id_records[student_id]
            elif student_name is not None:
                return self._name_records[student_name]

        except KeyError as error:
            raise KeyError("Record not found") from error

        raise KeyError("No information was supplied")

    def _add_to_inverse_index(self, full_name: str):
        names = full_name.split()
        for name_index, name in enumerate(names):
            name = name.lower()

            self._inverse_index.setdefault(name, [])
            self._inverse_index[name].append((full_name, name_index))

    def _remove_from_inverse_index(self, full_name: str):
        names = full_name.split()
        for name_index, name in enumerate(names):
            token_list = self._inverse_index[name.lower()]
            token_list.remove((full_name, name_index))

            if not token_list:
                self._inverse_index.pop(name.lower())

    def add_record(self, student_record: StudentRecord):
        self._ids.add(student_record.id())
        self._names.add(student_record.name())
        self._records.append(student_record)
        self._raw_records.append(student_record.raw())
        self._id_records[student_record.id()] = student_record
        self._name_records[student_record.name()] = student_record
        self._add_to_inverse_index(student_record.name())

    def remove_record(self, student_record: StudentRecord):
        self._ids.remove(student_record.id())
        self._names.remove(student_record.name())
        self._records.remove(student_record)
        self._raw_records.remove(student_record.raw())
        self._id_records.pop(student_record.id())
        self._name_records.pop(student_record.name())
        self._remove_from_inverse_index(student_record.name())

    def search_record(self, query: str):
        query = query.strip()
        query_names = query.split()
        maximum_differences = len(query) // 3

        if len(query_names) > 1:
            sorted_names = levenshtein_automaton(query, sorted(self.names()), maximum_differences)

        else:
            possible_names = levenshtein_automaton(query, sorted(self._inverse_index.keys()), maximum_differences)
            name_results = {full_name: order
                            for name in possible_names
                            for full_name, order in self._inverse_index[name]}
            sorted_names = *sorted(name_results, key=name_results.get),

        return RecordsTable([self.get_record(student_name=name) for name in sorted_names])

    def read_file(self, filename: str):
        with open(filename, "r") as file:
            line = file.readline().strip()

            while line:
                data = line.split(",")
                student_record = StudentRecord(student_id=int(data[0]), student_name=data[1].strip(),
                                               student_gpa=float(data[2]))

                self.add_record(student_record)

                line = file.readline().strip()

    def update_file(self, filename: str):
        with open(filename, "w") as file:
            for student_record in self._records:
                file.write(f"{student_record.id()}, {student_record.name()}, {student_record.gpa()}\n")

    def search_analyzer(self, response: str):
        possible_records = self.search_record(response)

        if not possible_records:
            print("No results")
            return Codes.BACK

        # Show data
        show_data(possible_records.raw())

        search_menu = Menu(back_option="Search Again")
        search_menu.add_option("Choose")
        choice_number, return_code = search_menu.display()

        if return_code == Codes.SUCCESS:
            return input("Enter ID: ")

        else:
            return return_code

    def present_id_check(self, response: str) -> tuple[bool, str]:
        try:
            student_id = int(response)

        except ValueError:
            return False, "the ID should be 9 integer numbers"

        if len(response) != 9:
            return False, "the ID should be 9 integer numbers"

        if student_id in self._ids:
            return True, ""

        else:
            return False, "the ID is not there"

    def new_id_check(self, response: str) -> tuple[bool, str]:
        try:
            student_id = int(response)

        except ValueError:
            return False, "the ID should be 9 integer numbers"

        if len(response) != 9:
            return False, "the ID should be 9 integer numbers"

        if student_id not in self._ids:
            return True, ""

        else:
            return False, "the ID is already there"


class Menu:

    def __init__(self, back_option: str = "Back"):
        self._back_option = back_option
        self._prompts: list[str] = []
        self._options: dict[int, ...] = {}

    def add_option(self, option_text: str, function=None, *args):
        self._prompts.append(option_text)
        option_number = len(self._prompts)

        if function:
            self._options[option_number] = wrap_function(function, *args)
        else:
            self._options[option_number] = None

    def valid_option(self, input_response: str, threshold: int) -> bool:
        return NotImplemented  # TODO Implement this

    def display(self, pre='', post='', default_question_override='', final='') -> tuple:
        if not default_question_override:
            default_question_override = "Enter a number to choose: "

        if pre:
            print(pre)

        for option_number, prompt in enumerate(self._prompts, start=1):
            print(f"{option_number} {prompt}")

        back_number = len(self._prompts) + 1
        print(f"{back_number} {self._back_option}")

        if post:
            print(post)

        choice_number = 0
        while True:
            response = input(default_question_override).strip()
            if not response.isdigit():
                print("Please enter a number only.")
                continue

            choice_number = int(response)
            if choice_number == back_number:
                return choice_number, Codes.BACK

            if choice_number not in self._options:
                print("Please enter a number that is present.")
            else:
                break

        if final:
            print(final)

        option = self._options[choice_number]
        if option is None:
            return choice_number, Codes.SUCCESS

        return_value = option()
        if return_value == Codes.BACK:
            return choice_number, Codes.INCONCLUSIVE

        else:
            return choice_number, return_value


class Inputs:

    def __init__(self):
        self._prompts = []
        self._inputs = {}

    def add_prompt(self, prompt_text: str, check, analyzer=None):
        self._inputs[prompt_text] = (analyzer, check)
        self._prompts.append(prompt_text)

    def take_inputs(self):
        print("Type 'cancel' to stop taking input or 'back' to undo.")

        results = [''] * len(self._prompts)

        current_prompt_index = 0
        while current_prompt_index < len(self._prompts):
            prompt = self._prompts[current_prompt_index]
            response = input(prompt)

            if response.lower() == "cancel" or (current_prompt_index == 0 and response.lower() == "back"):
                return Codes.BACK

            elif response.lower() == "back":
                current_prompt_index -= 1
                continue

            input_analyzer, input_check = self._inputs[prompt]
            if input_analyzer:
                analyzed_response = input_analyzer(response)
                if analyzed_response == Codes.BACK:
                    continue

            else:
                analyzed_response = response

            check_success, check_message = input_check(analyzed_response)
            if check_success:
                results.pop(current_prompt_index)
                results.insert(current_prompt_index, analyzed_response)
                current_prompt_index += 1

            else:
                print(check_message)

        return *results,


# TODO
#   Make this a general function so that we can print menus in an appealing format. The new general function should
#   take a list of dictionaries where each dict is a ROW and each key in the the dict is a COLUMN
#   Use the following to test:
#   >records = [
#   {'id': 123456789, 'name': 'mohammed khalifa', 'gpa': 2.25},
#   {'id': 202312340, 'name': 'khalid ahmed', 'gpa': 3.5},
#   {'id': 202345771, 'name': 'Mohammad Abdu', 'gpa': 0.0}
#   ]
#   >show_data(records)
#   _______________________________________
#   | ID        | Name             | GPA  |
#   _______________________________________
#   | 123456789 | mohammed khalifa | 2.25 |
#   | 202312340 | khalid ahmed     | 3.50 |
#   | 202345771 | Mohammad Abdu    | 0.00 |
#   _______________________________________

def show_data(student_id_records: dict[int, dict[str, str or float]]) -> tuple:
    print(student_id_records)
    return NotImplemented
    lines = []

    max_name_length = 0
    for student_record in student_id_records:
        name_length = len(student_id_records[student_record]["name"])
        if name_length > max_name_length:
            max_name_length = name_length

    lines.append("_" * (max_name_length + 23))
    lines.append(f"| ID        | Name{(max_name_length - 4) * ' '} | GPA  |")
    lines.append("_" * (max_name_length + 23))
    for student in student_id_records:
        lines.append(
            f"| {student:8d} | {student_id_records[student]['name']}"
            f"{(max_name_length - len(student_id_records[student]['name'])) * ' '} |"
            f" {student_id_records[student]['gpa']:4.2f} |")
    lines.append("_" * (max_name_length + 23))

    for line in lines:
        print(line)

    return Codes.SUCCESS, Codes.NO_RETURN


def wrap_function(function, *args):
    def wrapped_function(*args2):
        return function(*args, *args2)

    return wrapped_function


def search_ids(query: int):
    return NotImplemented  # TODO Implement this


if __name__ == "__main__":
    test_menu = Menu()
    test_menu.add_option("Haha")
    test_menu.add_option("gogo")
