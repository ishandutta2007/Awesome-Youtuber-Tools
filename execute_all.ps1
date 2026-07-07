$ErrorActionPreference = "Continue"

python modify_readme_step1.py
git add . ;git commit -m "Added company size and sorted the SaaS based on that";git push;

python modify_readme_step2.py
git add . ;git commit -m "Added github stars and sorted the opensource based on that";git push;

python modify_readme_step3.py
git add .  && git commit -m "added emojis and banner" && git push

python modify_readme_step4.py
git add .  && git commit -m "seo optimised and badges to left added" && git push

python modify_readme_step5.py
git add .  && git commit -m "badges to right added" && git push

python modify_readme_step6.py
git add . ;git commit -m "star history added";git push;

python modify_readme_step7.py
git add . ;git commit -m "fixed star plot";git push;

python modify_readme_step8.py
git add . ;git commit -m "invalid awesome link fixed";git push;
