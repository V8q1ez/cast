Feature: Compare
  In order to be sure that c-files are identical,
  As a software developer
  I want to compare two c-files with differences
  in comments and white characters and to get
  the result of compare operation

  Scenario: Completely Identical Files
    Given the left and right files are completely identical
     When the 'cast compare' is performed
     Then the output shall contain 'Files are equivalent'
