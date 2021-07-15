# network_classifier
Hi! Network Classifier was really fun.

# Design
![image](https://user-images.githubusercontent.com/35425887/125861734-1efa9c37-2a65-4cc0-b4e0-42eee559cfbd.png)

[Network Classifier design.pdf](https://github.com/reahaas/network_classifier/files/6826330/Network.Classifier.design.pdf)

# Tests
to run the tests you first need to run the file 
`tests/install_tests_dependencies.sh`

The to run the test: 
`python3 -m pytest tests`

![image](https://user-images.githubusercontent.com/35425887/125860693-39e643ba-9563-46e7-bcd4-fdd63e9acf00.png)



# Done:
1. runner.sh to run the script.
2. define data_types.py: Communications, Rules, Classifications.
3. read from files to list of data (namedtuples).
4. Identify rule matching -> give list of `Classifications`.
5. write the Classifications list to file.
6. tests:
    a. End to End test: runner test, all the flow.
    b. Unit test: RuleMatcher functionality.

# Todo:
1. Implement `get_final_classifications`
2. Add support for rule type "multi_rules".
3. Reorder the code to work with concurrecy.
4. More tests.
