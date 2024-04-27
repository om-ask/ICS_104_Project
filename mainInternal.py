from searchInternal import levenshtein_automaton


class Back(BaseException):
    """An exception to raise when a user wants to go back in a menu or when taking input
    """
    pass


class StudentRecord:
    """Objects of this class each store information of one single student"""

    def __init__(self, student_id: int, student_name: str, student_gpa: float):
        """Initialize the class with the student info given
        """
        # All the following attributes are private
        self._id: int = student_id
        self._name: str = student_name
        self._gpa: float = student_gpa
        # A dictionary with all the student info
        self._raw: dict[str, ...] = {"ID": self._id, "Name": self._name, "GPA": self._gpa}

    def id(self) -> int:
        """Return the student's id
        """
        return self._id

    def name(self) -> str:
        """Return the student's name
        """
        return self._name

    def gpa(self) -> float:
        """Returns the student's GPA
        """
        return self._gpa

    def raw(self) -> dict:
        """Returns a dictionary with ID, Name, GPA as keys associated with their respective values
        """
        return self._raw

    def modify_gpa(self, new_gpa: float):
        """Updates the students GPA to the new GPA given
        """
        self._gpa = new_gpa
        self._raw["GPA"] = new_gpa  # Update the raw dictionary


class RecordsTable:
    """Objects of this class store a variable number of StudentRecords and allows different operation on the stored
    student records such as searching, adding, removing, modifying etc."""

    def __init__(self, records_list=None):
        # Initialize private containers for data from the students
        self._ids: set[int] = set()  # A unique set of all student ids
        self._names: set[str] = set()  # A unique set of all student names
        self._records: list[StudentRecord] = []  # A list of student records (StudentRecord)
        self._raw_records: list[dict[str, ...]] = []  # A list of raw student information as dictionaries
        self._id_records: dict[int, StudentRecord] = {}  # A dictionary with ids as keys and student info as values
        self._name_records: dict[str, StudentRecord] = {}  # A dictionary with names as keys and student info as values
        self._inverse_index: dict[str, list[tuple]] = {}  # An index with single names as keys and full names as values
        # The full names are in a tuple with the first element being the full name and the second being the index of the
        # single name in the full name
        # This inverse index is only used when doing quick partial searches for student names

        # This stores the last used filename when reading or updating a file
        self.filename: str = ""

        # If a list of records was given, add them
        if records_list:
            for record in records_list:
                self.add_record(record)

    def records(self) -> list[StudentRecord]:
        """Returns a list of student info (StudentRecord)
        """
        return self._records

    def names(self) -> set[str]:
        """Returns a set of all student names
        """
        return self._names

    def ids(self) -> set[int]:
        """Returns a set of all student ids
        """
        return self._ids

    def raw(self) -> list[dict[str, ...]]:
        """Returns a list of dictionaries where each dictionary contains info for a single student in the format of:
        {"ID": student_id, "Name": student_name,"GPA": student_gpa}
        This is mainly used with show_data() in order to display the student info
        """
        return self._raw_records

    def get_record(self, student_id=None, student_name=None) -> StudentRecord:
        """Given an id or a name, returns a student if found. If not found then a KeyError is raised
        """
        try:
            if student_id is not None:
                # If an id was provided then fetch the student from the id dictionary
                return self._id_records[student_id]
            elif student_name is not None:
                # If an id was provided then fetch the student from the name dictionary
                return self._name_records[student_name]

        except KeyError as error:
            # Raise an error
            raise KeyError("Record not found") from error

        # If no id or name was supplied, raise an error
        raise KeyError("No information was supplied")

    def _add_to_inverse_index(self, full_name: str):
        """Given a full student name, adds each part of the name into the inverse index
        """
        # Split to each part
        names = full_name.split()

        # Iterate over each part
        for name_index, name in enumerate(names):
            name = name.lower()  # Set to lowercase

            # If the single name part is not present then set it
            self._inverse_index.setdefault(name, [])

            # Add to the inverse index the full name and the order of the part in the full name
            self._inverse_index[name].append((full_name, name_index))

    def _remove_from_inverse_index(self, full_name: str):
        """Removes a given full name from the inverse index
        """
        # Split to each part
        names = full_name.split()

        # Iterate over each part
        for name_index, name in enumerate(names):
            # Get all the full names for that part in the inverse index
            token_list = self._inverse_index[name.lower()]

            # Remove this specific full name
            token_list.remove((full_name, name_index))

            # If the list for the part in the index is empty after removal, delete it
            if not token_list:
                self._inverse_index.pop(name.lower())

    def clear(self):
        """Clears and deletes all student info
        """
        # Empty every single private container
        self._ids.clear()
        self._names.clear()
        self._records.clear()
        self._raw_records.clear()
        self._id_records.clear()
        self._name_records.clear()
        self._inverse_index.clear()

    def add_record(self, student_record: StudentRecord):
        """Add a student (StudentRecord)
        """
        # Add to each private container
        self._ids.add(student_record.id())
        self._names.add(student_record.name())
        self._records.append(student_record)
        self._raw_records.append(student_record.raw())
        self._id_records[student_record.id()] = student_record
        self._name_records[student_record.name()] = student_record
        self._add_to_inverse_index(student_record.name())

    def remove_record(self, student_record: StudentRecord):
        """Remove a student (StudentRecord)
        """
        # Remove from each private containers
        self._ids.remove(student_record.id())
        self._names.remove(student_record.name())
        self._records.remove(student_record)
        self._raw_records.remove(student_record.raw())
        self._id_records.pop(student_record.id())
        self._name_records.pop(student_record.name())
        self._remove_from_inverse_index(student_record.name())

    def search_record(self, query: str):
        """Returns a new RecordsTable with all the students that match the search query
        """
        query = query.strip()
        query_names = query.split()
        maximum_differences = len(query) // 3

        if len(query_names) > 1:
            sorted_names = levenshtein_automaton(query, sorted(self.names()), maximum_differences)

        else:
            possible_names = levenshtein_automaton(query, sorted(self._inverse_index.keys()), maximum_differences)
            name_results = {full_name: order
                            for name in possible_names
                            for full_name, order in self._inverse_index[name.lower()]}
            sorted_names = *sorted(name_results, key=name_results.get),

        return RecordsTable([self.get_record(student_name=name) for name in sorted_names])

    def read_file(self, filename: str):
        """Reads the file given if found into the records
        """
        self.filename = filename  # Update the current filename

        # Open in read mode
        with open(filename, "r") as file:
            # Read the first line
            line = file.readline().strip()

            # Loop until the end of the file (line becomes empty)
            while line:
                # Split the line
                data = line.split(",")
                # The first, second, and third index in the split line should the ID, Name, GPA respectively
                # Create a new StudentRecord with the info
                student_record = StudentRecord(student_id=int(data[0]), student_name=data[1].strip(),
                                               student_gpa=float(data[2]))

                # Add it to self
                self.add_record(student_record)

                # Read the next line
                line = file.readline().strip()

    def update_file(self, filename=None):
        """Updates the file if given, otherwise updates the file given when making the object for the first time
        """
        # If no filename was given then default to the filename in self
        if not filename:
            filename = self.filename

        # Open file in write mode
        with open(filename, "w") as file:
            # Iterate over every record
            for student_record in self._records:
                # Write a line in the correct format for each student:
                # ID, Name, GPA
                file.write(f"{student_record.id()}, {student_record.name()}, {student_record.gpa()}\n")

    def search_analyzer(self, response: str):
        possible_records = self.search_record(response)

        if not possible_records.records():
            print("No results")
            raise Back

        # Show data
        show_data(possible_records.raw())

        choice_number = menu(["Choose"], back_option="Search Again")

        if choice_number == 1:  # Option Choose
            return input("Enter ID: ")

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


class Inputs:

    def __init__(self):
        self._prompts = []
        self._inputs = {}

    def add_prompt(self, prompt_text: str, check, analyzer=None):
        self._inputs[prompt_text] = (analyzer, check)
        self._prompts.append(prompt_text)

    def take_inputs(self):
        print("Type 'cancel' to stop taking input or 'back' to undo.")

        results = [None] * len(self._prompts)

        current_prompt_index = 0
        while current_prompt_index < len(self._prompts):
            prompt = self._prompts[current_prompt_index]
            response = input(prompt)

            if response.lower() == "cancel" or (current_prompt_index == 0 and response.lower() == "back"):
                raise Back

            elif response.lower() == "back":
                current_prompt_index -= 1
                continue

            input_analyzer, input_check = self._inputs[prompt]
            if input_analyzer:
                try:
                    analyzed_response = input_analyzer(response)
                except Back:
                    continue

            else:
                analyzed_response = response

            if input_check is None:
                results.pop(current_prompt_index)
                results.insert(current_prompt_index, analyzed_response)
                current_prompt_index += 1
                continue

            check_success, check_message = input_check(analyzed_response)
            if check_success:
                results.pop(current_prompt_index)
                results.insert(current_prompt_index, analyzed_response)
                current_prompt_index += 1

            else:
                print(check_message)

        if len(results) > 1:
            return tuple(results)
        else:
            return results[0]


def menu(options: list[str], back_option: str = "Back",
         prompt="Enter a number to choose or type in part of the option: ") -> int:
    """Displays the options given and prompts the user.
    Returns an integer indicating the option selected starting from 1
    Raise Back (error) if the user chooses the back option

    Give the options as a list of strings that will be displayed
    """
    # Prepare the options as a table to be shown using view_data()
    display_data = []
    for option_number, option in enumerate(options, start=1):
        display_data.append({"Number": option_number, "Option": option})

    # Add the back option
    display_data.append({"Number": 0, "Option": back_option})
    options = [back_option] + options

    # Display the data
    show_data(display_data)

    # Loop until a valid option is chosen
    while True:
        # Take a response from the user
        response = input(prompt).strip()

        if response.isdigit():
            # If the response is a number, check if the number is present
            choice_number = int(response)
            if choice_number == 0:  # If the user chooses back, raise Back
                print("Chose Option", back_option)
                raise Back

            elif 0 < choice_number < len(options):  # If the user chose a valid number, return the choice
                print(f"Chose Option {choice_number}: {options[choice_number]}")
                return choice_number

            else:  # Otherwise, notify the user and retake input
                print("Please enter a number that is present.")

        else:
            # If the response is not a number, search for it within the options
            possible_options = levenshtein_automaton(response, sorted(options), 0)
            if possible_options:  # If there are possible options
                # Take the most possible option
                option = possible_options[0]

                # Check where the option lies in the options list
                choice_number = options.index(option)

                if choice_number == 0:  # If the user chooses back, raise Back
                    print("Chose Option", back_option)
                    raise Back

                else:  # If the option is
                    print(f"Chose Option {choice_number}: {option}")
                    return choice_number

            else:  # Otherwise, notify the user and retake input
                print("Please type in a valid choice.")


def show_data(data: list[dict[str, ...]]):
    """Prints data formatted as a list of dictionaries, where each dictionary in the list is a row and each
    key in the dictionary a column.

    *Note: Each dictionary should have identical keys.

    Example input and output:

    >records = [
    {'ID': 123456789, 'Name': 'mohammed khalifa', 'Gpa': 2.25},
    {'ID': 202312340, 'Name': 'khalid ahmed', 'Gpa': 3.5},
    {'ID': 202345771, 'Name': 'Mohammad Abdu', 'Gpa': 0.0}
    ]
    >show_data(records)
    _______________________________________
    | ID        | Name             | GPA  |
    _______________________________________
    | 123456789 | mohammed khalifa | 2.25 |
    | 202312340 | khalid ahmed     | 3.50 |
    | 202345771 | Mohammad Abdu    | 0.00 |
    _______________________________________
    """
    column_titles = []
    columns_max_width = {}

    if not data:
        print("There is no data to show\n\n")
        return

    # Get the column titles for the data to display
    for title in data[0]:
        column_titles.append(title)
        columns_max_width[title] = len(title)

    # Get the maximum width of each column in the data
    for row in data:
        for title in column_titles:
            if len(str(row[title])) > columns_max_width[title]:
                columns_max_width[title] = len(str(row[title]))

    # Get the max row length in the table
    max_line_length = 1 + sum(list(columns_max_width.values())) + 3 * len(column_titles)
    row_boundary = max_line_length * "_"

    # Print the header
    print(row_boundary)
    for title in column_titles:
        print(f"| {title}{' ' * (columns_max_width[title] - len(title))} ", end="")
    print("|")

    # Print the table rows
    print(row_boundary)
    for row in data:  # rows
        for column in column_titles:
            print(f"| {row[column]}{' ' * (columns_max_width[column] - len(str(row[column])))} ", end="")
        print("|")

    # Close the table
    print(row_boundary)
    print()


def valid_name_check(response: str) -> tuple[bool, str]:
    if len(response.split()) >= 2:
        return True, ""
    else:
        return False, "Please enter at least a first and second name."


def valid_gpa_check(response: str) -> tuple[bool, str]:
    try:
        student_gpa = float(response)

    except ValueError:
        return False, "The GPA should be a number between 0 and 4"

    if 0 <= student_gpa <= 4:
        return True, ""
    else:
        return False, "The GPA should be a number between 0 and 4"


def valid_filename_check(response: str) -> tuple[bool, str]:
    parts = response.split(".")  # Split the file
    for part in parts:
        if not part.isalnum():
            return False, "Please enter only alphanumeric characters for the filename."

    return True, ''


def create_file(filename):
    """Creates a file with the name filename if not present.
    Goes back if an error occurs.
    """
    try:
        # Open filename with mode 'w' in order to create the file if it is not present
        with open(filename, mode="w"):
            pass   # Do nothing

    except IOError:
        # In case an error occurs, go back
        print(f"Could not create '{filename}'")
        raise Back

    else:
        # If the file was successfully created, notify the user
        print(f"Successfully created/opened file '{filename}'")
        print()


def read_file_into_record(records: RecordsTable, filename: str = ""):
    """Reads file contents and updates records with the data in it. If the file could not be opened or something wrong
    happens, prompts the user with options.
    Supports going back
    """
    # Define an input for taking in filenames from the user in case the current file cannot be opened for any reason
    new_file_name_input = Inputs()
    new_file_name_input.add_prompt("Enter a new filename: ", valid_filename_check)

    # Take a filename if no filename was provided
    if not filename:
        filename = new_file_name_input.take_inputs()

    # Read from file until successful while handling any errors
    while True:
        try:
            # Attempt to read file
            records.read_file(filename=filename)

            # If no error occurs, print message and exit
            print(f"Successfully opened and read from file '{filename}'")
            print()
            return

        except FileNotFoundError:
            # If the file is not found, notify user
            print(f"ERROR: Could not find file '{filename}'")
            print()

            # Prompt the user to either choose to create a new file or to set a new file to read from
            print("Do you want to?")
            choice_number = menu([f"Create File '{filename}'", "Set New Filename"])
            print("\n")

            if choice_number == 1:  # Option Create File
                create_file(filename)

            else:  # Option Set New Filename
                # Set a new filename to attempt again
                filename = new_file_name_input.take_inputs()

        except IndexError:
            # If the file is not formatted correctly, notify user and take a new file
            print(f"ERROR: '{filename}' File format is incorrect")
            print()
            # Set a new filename to attempt again
            filename = new_file_name_input.take_inputs()

        except IOError:
            # Catch any other error and notify user
            print(f"ERROR: Unexpected error occurred while trying to read '{filename}'")
            print()
            # Set a new filename to attempt again
            filename = new_file_name_input.take_inputs()


def update_file_from_record(filename, records: RecordsTable):
    """Opens file and updates its data with the records. If the file could not be opened, prompts the user
    for a new file.
    Supports going back
    """
    # Define an input for taking in filenames from the user in case the current file cannot be opened for any reason
    new_file_name_input = Inputs()
    new_file_name_input.add_prompt("Enter a new filename: ", valid_filename_check)

    # Attempt to update file until successful
    while True:
        try:
            # Attempt updating
            records.update_file(filename)
            # If successful then exit
            print(f"Successfully updated file '{filename}'")
            print()
            return

        except IOError:
            # If any file error occurs, prompt the user for a new filename
            print(f"ERROR: Could not write to '{filename}'")
            filename = new_file_name_input.take_inputs()


def write_to_new_file(records: RecordsTable):
    inputs = Inputs()
    inputs.add_prompt("Enter the new file name:", valid_filename_check)

    file_name = inputs.take_inputs()
    update_file_from_record(file_name, records)

def switch_file(records: RecordsTable):
    records.clear()
    inputs = Inputs()
    inputs.add_prompt("Enter the new file name:", valid_filename_check)

    file_name = inputs.take_inputs()
    read_file_into_record(records, file_name)

if __name__ == "__main__":
    a = test_menu = menu(["Haha", "gogo"])
    print("o", a)
