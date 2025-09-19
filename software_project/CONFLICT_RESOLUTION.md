# Calculator Conflict Resolution

## What Caused The Error
The error was caused in the calculator.py file in the add function. There were changes happening on the same line so the merge couldn't go through. The differences were the following:

return a + b + 1

return a + b - 1

## How to Fix Merge Conflict Error
After trying to push the cloned repo, it gave me an error and after pulling the code down, it showed me markers where there was an isuse. I had to get rid of the markers and manually fix the code and choose which one I wanted to keep or how I wanted to push the code to GitHub. In most scenarios, you'd choose one and erase the other or find a compromise, but in this scenario, since both codes were wrong, I removed both of them and just left it to be return a + b as that is the correct code for the add function.

I then added the file, committed it, and pushed it to GitHub for it to work

## Second Conflict Resolution For README
This conflict happened when I was merging the hotfix/readme-update branch into the main branch. It happened because this branch was created in the cloned repo and I guess I forgot to pull in previous changes into it so when I tried merging it into main, I got this conflict error. Just as background info, when I manually created the title conflict for README earlier, the first push I added (change change) to the title and the other push I added (modify modify modify) to it. I was sort of confused about the instructions saying keep both titles in a meaningful way and combine both titles after it so I just kept both titles in different lines then had a third line that combined both of them. So now back to this conflict error, this is what it looked like

    Main repo:
    # My Software Engineering Project (change change)
    # My Software Engineering Project (modify modify modify)
    # My Software Engineering Project (change change modify modify modify)

    hotfix/readme-update repo:
    # My Software Engineering Project (modify modify modify)

## How To Fix This Conflict Error
Since I forgot to pull down the README earlier for the cloned repo, I just had to remove what the old repo said and leave what the main one had as that was the one I wanted to keep. I then added the file, committed it, pushed it, and was able to merge successfully after.

