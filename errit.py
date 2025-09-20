#!/bin/env python3
import argparse
import praw
from praw.models import Submission, Comment
import datetime
from rich.console import Console


def main():
    styles = {
        "comment_content": "yellow",
        "submission_content": "yellow",
        "post_date": "green",
        "post_title": "white",
        "subreddit": "orange",
    }
    console = Console()
    parser = argparse.ArgumentParser(description="Explore your saved Reddit posts.")
    parser.add_argument("reddit_account", help="The Reddit account to explore.")
    parser.add_argument(
        "--num_posts",
        type=int,
        default=10,
        help="The number of posts to get (default: 10).",
    )
    parser.add_argument(
        "--subreddit",
        type=str,
        default="",
        help="The subreddit to filter by.",
    )

    args = parser.parse_args()

    console.print(f"Reddit Account: {args.reddit_account}")
    console.print(f"Number of posts: {args.num_posts}")
    if args.subreddit:
        console.print(f"Filtering by subreddit: {args.subreddit}")

    try:
        reddit = praw.Reddit(args.reddit_account)
        user = reddit.user.me()
        if user is None:
            console.print(
                "Error: Could not retrieve user information. Please check your Reddit account credentials."
            )
            exit(1)
        console.print(user)
        for i, saved_post in enumerate(user.saved(limit=args.num_posts)):
            if (
                args.subreddit
                and saved_post.subreddit.display_name.lower() != args.subreddit.lower()
            ):
                continue
            if isinstance(saved_post, Submission):
                header = f"{i + 1}. Subreddit: [{styles['subreddit']}]{saved_post.subreddit.display_name}[/] - Post Date: [{styles['post_date']}]{datetime.datetime.fromtimestamp(saved_post.created_utc)}[/]"
                console.print(header)
                console.print(f"Post: [{styles['post_title']}]{saved_post.title}[/]")
            elif isinstance(saved_post, Comment):
                header = f"{i + 1}. Subreddit: [{styles['subreddit']}]{saved_post.subreddit.display_name}[/] - Comment Date: [{styles['post_date']}]{datetime.datetime.fromtimestamp(saved_post.created_utc)}[/] - Post Title: [{styles['post_title']}]{saved_post.submission.title}[/] - Post Date: [{styles['post_date']}]{datetime.datetime.fromtimestamp(saved_post.submission.created_utc)}[/]"
                console.print(header)
                console.print(
                    f"Comment: [{styles['comment_content']}]{saved_post.body}[/]"
                )
            else:
                console.print(f"{i + 1}. Unknown type: {type(saved_post)}")

    except Exception as e:
        console.print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
