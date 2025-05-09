import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--tutorial_name", type=str, default=None)
args = parser.parse_args()

print(args)


if not args.tutorial_name:
    links = {}
    for tutorial_name in os.listdir():
        if os.path.isdir(tutorial_name) and 'tutorial' in tutorial_name:
            for sub_folder in os.listdir(tutorial_name):
                if 'part' in sub_folder and os.path.isdir(os.path.join(tutorial_name, sub_folder)):
                    for file in os.listdir(os.path.join(tutorial_name, sub_folder)):
                        if file.endswith(".ipynb"):
                            # complete_link, starter_link = None, None
                            if 'complete' in file:
                                complete_link = f'https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FAPS106%2FAPS106-summer-2025-tutorials&urlpath=tree%2FAPS106-summer-2025-tutorials%2F{tutorial_name}%2F{sub_folder}%2F{file}&branch=main'
                            elif 'starter' in file:
                                starter_link = f'https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FAPS106%2FAPS106-summer-2025-tutorials&urlpath=tree%2FAPS106-summer-2025-tutorials%2F{tutorial_name}%2F{sub_folder}%2F{file}&branch=main'
                            
                    links[f'{tutorial_name}/{sub_folder}/{file}'] = (starter_link, complete_link)

    with open('links.txt', 'w') as f:
        for file, (starter_link, complete_link) in links.items():
            f.write(f"{file}\n{starter_link}\n{complete_link}\n\n")

else:
    links = {}
    for file in os.listdir(args.tutorial_name):
        if file.endswith(".ipynb"):
            if 'complete' in file:
                complete_link = f'https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FAPS106%2FAPS106-summer-2025-tutorials&urlpath=tree%2FAPS106-summer-2025-tutorials%2F{args.tutorial_name}%2F{file}&branch=main'
            elif 'starter' in file:
                starter_link = f'https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FAPS106%2FAPS106-summer-2025-tutorials&urlpath=tree%2FAPS106-summer-2025-tutorials%2F{args.tutorial_name}%2F{file}&branch=main'
            links[f'{args.tutorial_name}/{file}'] = (starter_link, complete_link)

    if os.path.exists("links.txt"):
        with open("links.txt", "r") as f:
            for file, (starter_link, complete_link) in links.items():
                f.write(f"{file}\n{starter_link}\n{complete_link}\n\n")
    else:
        with open("links.txt", "w") as f:
            for file, (starter_link, complete_link) in links.items():
                f.write(f"{file}\n{starter_link}\n{complete_link}\n\n")

# link_starter = f'https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FAPS106%2FAPS106-summer-2025-tutorials&urlpath=tree%2FAPS106-summer-2025-tutorials%2F{TUTORIAL-NAME}%2F{SUB-FOLDER}%2F{FILENAME}&branch=main'
# # read/create txt file with links
# if os.path.exists("links.txt"):