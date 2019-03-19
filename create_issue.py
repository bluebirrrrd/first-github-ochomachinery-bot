import asyncio
import os
from octomachinery.github.api.tokens import GitHubOAuthToken
from octomachinery.github.api.raw_client import RawGitHubAPI

async def main():
    access_token = GitHubOAuthToken(os.environ["GITHUB_TOKEN"])
    gh = RawGitHubAPI(access_token, user_agent='bluebirrrrd')
    await gh.post('/repos/mariatta/strange-relationship/issues',
        data={
            'title': 'We got a problem',
            'body': 'Use more emoji!',
        })

loop = asyncio.get_event_loop()
loop.run_until_complete(main())