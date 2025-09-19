import argparse
import praw

def main():
    parser = argparse.ArgumentParser(description='Explore your saved Reddit posts.')
    parser.add_argument('reddit_account', help='The Reddit account to explore.')
    parser.add_argument('--num_posts', type=int, default=10, help='The number of posts to get (default: 10).')

    args = parser.parse_args()

    reddit = praw.Reddit("bot1")

    print(f"Reddit Account: {args.reddit_account}")
    print(f"Number of posts: {args.num_posts}")

if __name__ == '__main__':
    main()
