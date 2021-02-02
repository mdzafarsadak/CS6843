### welcome_assignment_answers
### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    # The student doesn't have to follow the skeleton for this assignment.
    # Another way to implement is using a "case" statements similar to C.
    if question == "Are encoding and encryption the same?":
        answer = "Yes"
    elif question == "Is it possible to decrypt a message without a key?":
        answer = "No"

    elif question == "Is it possible to decode a message without a key?":
        answer = "No"

    elif question == "Is a hashed message supposed to be un-hashed?":
        answer = "No"

    elif question == "What is the MD5 hashing value to the following message:":

        answer = "42b76fe51778764973077a5a94056724"

    elif question == "Is MD5 a secured hashing algorithm?":
        answer = "Yes"

    elif question == "What layer from the TCP/IP model the protocol DHCP belongs to?":
        answer = 1

    elif question == "What layer of the TCP/IP model the protocol TCP belongs to?":
        answer = 4
    return (answer)



# Complete all the questions.


if __name__ == "__main__":
    # use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same?"
    print(debug_question)
    print(welcome_assignment_answers(debug_question))

    debug_question = "Is it possible to decrypt a message without a key?"
    print(debug_question)
    print(welcome_assignment_answers(debug_question))

    debug_question = "Is it possible to decode a message without a key?"
    print(debug_question)
    print(welcome_assignment_answers(debug_question))

    debug_question = "Is a hashed message supposed to be un-hashed?"
    print(debug_question)
    print(welcome_assignment_answers(debug_question))

    debug_question = "What is the MD5 hashing value to the following message:"
    print(debug_question)
    print(welcome_assignment_answers(debug_question))

    debug_question = "Is MD5 a secured hashing algorithm?"
    print(debug_question)
    print(welcome_assignment_answers(debug_question))

    debug_question = "What layer from the TCP/IP model the protocol DHCP belongs to?"
    print(debug_question)
    print(welcome_assignment_answers(debug_question))

    debug_question = "What layer of the TCP/IP model the protocol TCP belongs to?"
    print(debug_question)
    print(welcome_assignment_answers(debug_question))
