# --- Import required libraries / modules:
import argparse         # https://docs.python.org/3/library/argparse.html


def main() -> None:
    # --- Instantiate the argument parser:
    parser = argparse.ArgumentParser(prog = 'show_name',
                                    description = 'This program will take your name and print it out',
                                    add_help = True)

    # --- Add an argument for the first name:
    parser.add_argument("--first-name", "-f",
                        type = str, 
                        help = "Enter your first name",
                        default = "John", # Only works if required is set to false.
                        nargs = "?",
                        required = False)

    # --- Add an argument for the last name:
    parser.add_argument("--last-name", "-l",
                        type = str, 
                        help = "Enter your last name",
                        nargs = "?",
                        required = True)

    # --- Build the results from the arguments passed (uses "dest =" from each argument):
    results = parser.parse_args()

    def build_name(results: object) -> str:
        """_summary_
        A simple function to display a greeting with the persons full name.
        
        Args:
            results (object): The object that is generated from the parser.

        Returns:
            str: A string saying 'Hello <first-name> <last-name>'
        """
        
        return f"Hello {results.first_name} {results.last_name}"

    # --- Display the name entered:
    print(build_name(results=results))


# --- Run the program:
if __name__ == "__main__":
    main()


"""
Notes:
=======

- If multiple flags for the same argument are passed, the last one entered will be used.
- Passing no value into an argument will result in the value being None.

"""