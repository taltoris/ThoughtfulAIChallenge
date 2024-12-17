# ThoughtfulAIChallenge

This is Doug LaMaster's entry to the ThoughtfulAI challenge hosted here:

https://thoughtfulautomation.notion.site/Platform-Technical-Screen-b61b6f6980714c198dc49b91dd23d695

Which is for the job posting here:

https://www.thoughtful.ai/job?gh_jid=4467861005&amp;gh_src=19c4d2c75us

# Explaination

The function sort takes four arguments: width, height, length, and mass, representing the dimensions and mass of the package, respectively.
It calculates the volume of the package by multiplying its dimensions.
 - A package is considered bulky if its volume is greater than or equal to 1,000,000 cm³ or if any of its dimensions are greater than or equal to 150 cm.
 - A package is considered heavy if its mass is greater than or equal to 20 kg.

Based on these conditions, the function determines the appropriate stack for the package:
 - If the package is both bulky and heavy, it is rejected.
 - If the package is either bulky or heavy (but not both), it is sent to the special stack.
 - If the package is neither bulky nor heavy, it is sent to the standard stack.

Test Cases
The provided example usage demonstrates the function's behavior with different inputs. You can add more test cases as needed to ensure the function handles various scenarios correctly.
