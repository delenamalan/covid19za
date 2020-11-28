"""
Used for automated data checks.
"""
from danger_python import danger, markdown

title = danger.github.pr.title
markdown(title)