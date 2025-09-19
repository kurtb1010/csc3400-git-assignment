# Calculator Conflict Resolution

## What Caused The Error
The error was caused in the calculator.py file in the add function. There were changes happening on the same line so the merge couldn't go through. The differences were the following:

return a + b + 1

return a + b - 1

## How to Fix Merge Conflict Error
After trying to push the cloned repo, it gave me an error and after pulling the code down, it showed me markers where there was an isuse. I had to get rid of the markers and manually fix the code and choose which one I wanted to keep or how I wanted to push the code to GitHub. In most scenarios, you'd choose one and erase the other or find a compromise, but in this scenario, since both codes were wrong, I removed both of them and just left it to be return a + b as that is the correct code for the add function.

I then added the file, committed it, and pushed it to GitHub for it to work.

