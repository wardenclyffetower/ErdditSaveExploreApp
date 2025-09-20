#!/bin/env python3
import argparse
import praw
from praw.models import Submission, Comment


def main():
    parser = argparse.ArgumentParser(description="Explore your saved Reddit posts.")
    parser.add_argument("reddit_account", help="The Reddit account to explore.")
    parser.add_argument(
        "--num_posts",
        type=int,
        default=10,
        help="The number of posts to get (default: 10).",
    )

    args = parser.parse_args()

    print(f"Reddit Account: {args.reddit_account}")
    print(f"Number of posts: {args.num_posts}")

    try:
        reddit = praw.Reddit(args.reddit_account)
        user = reddit.user.me()
        if user is None:
            print(
                "Error: Could not retrieve user information. Please check your Reddit account credentials."
            )
            exit(1)
        print(user)
        for i, saved_post in enumerate(user.saved(limit=args.num_posts)):
            if isinstance(saved_post, Submission):
                print(f"{i + 1}. Post: {saved_post.title}")
            elif isinstance(saved_post, Comment):
                print(f"{i + 1}. Comment: {saved_post.body}")
            else:
                print(f"{i + 1}. Unknown type: {type(saved_post)}")

    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
