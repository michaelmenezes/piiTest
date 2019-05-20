# piiTest
Validate the PII (Personally Identifiable Information) problem.

The PII Problem 
Process PII (Personally Identifiable Information) into JSON documents. Please use Java (Backend Roles), JavaScript (Frontend Roles), Python (Data Science Roles) to solve this problem. Extra credits for well thought out design, attention to quality and show casing your experience.
Input to your program 
A file with each line contains “PII”, information, which consists of a first name, last name, phone number, favorite color and zip code. The order and format of these lines vary in several ways, but for this test, the following three different formats are observed: 
	•	LastName, FirstName, (703)-711-0996, Blue, 11013 is a valid line
	•	LastName, FirstName, 12023, 636 121 1111, Yellow is an invalid line
	•	FirstName LastName, Purple, 14537, 713 905 0383 is a valid line
Input file may contain invalid lines and should not interfere with the processing of subsequent valid lines. For example, a line is invalid if its phone number does not contain the proper number of digits. We expect you make meaningful assumptions to arrive at an acceptable solution. 
Output from your program 
The program outputs a valid, formatted JSON object. The JSON representation should be indented with 2 space and the keys should be sorted in ascending alphabetical order by (last name, first name) 
Successfully processed lines should result in a normalized addition to the list associated with the “entries” key. For lines that were unable to be processed, a line number i (where 0 ≤ i < n) for each faulty line should be appended to the list associated with the “errors” key. 
Important note: Please format the JSON with exactly two spaces for every indentation. Our automated tests will not pass otherwise. Your program must execute the following way 
Solution < inputfile.txt > outpufile.txt or Solution –in inputfile.txt -out outpufile.txt Attached are the sample input and output files. Please submit a zip file or a Git Repository with your solution. 

    Usage: piiTest.py <input_file>, <output_file>
    Where the input_file is a list of entries in the format above and the output_file is a JSON object, sorted as mentioned above (ascending lastname, firstname) and with indent of 2 spaces.

Some Assumptions:
1. Any input not in the above 2 valid formats will be rejected as invalid.
2. Both the phone formats are supported in either line formats.
3. An area code that starts with a '0' or a '1' is acceptable to support the example. In reality there are no area codes in the USA that start with a '0' or a '1'.
4. The ZIP code is an USA centric 5 digit number. The number is not being validated to make sure it is a valid zip code against a know list.
5. The color field is any string. It will be good to have a predefined set of acceptable colors.
