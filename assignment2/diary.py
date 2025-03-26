# Task 1

import traceback

def main():
    try:
        # Open a file called diary.txt for appending.
        # Open the file using a with statement (inside the try block), and rely on that statement to handle the file close.
        with open("diary.txt",'a') as diary_file:
            # In a loop, prompt the user for a line of input. The first prompt should say, "What happened today? ". 
            prompt = "What happened today? "
            while True:
                # The input statement should be inside the loop inside the with block.
                entry = input(prompt)
                # As each line is received, write it to diary.txt, with a newline (\n) at the end.
                diary_file.write(entry + "\n")

                # All subsequent prompts should say "What else? "
                # When the special line "done for now" is received, write that to diary.txt. Then close the file and exit the program (you just exit the loop).
                if entry == "done for now":
                    break
                prompt = "What else? "

    # exception handing using the traceback module
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

if __name__ == "__main__":
    main()