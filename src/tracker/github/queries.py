"""GraphQL query documents for GitHub."""

ORG_REPOS = """
query($org: String!, $cursor: String) {
  organization(login: $org) {
    login
    repositories(first: 50, after: $cursor, orderBy: {field: PUSHED_AT, direction: DESC}) {
      pageInfo { hasNextPage endCursor }
      nodes {
        name
        nameWithOwner
        description
        isArchived
        isFork
        stargazerCount
        pushedAt
        defaultBranchRef { name }
        url
      }
    }
  }
}
"""

REPO_META = """
query($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    nameWithOwner
    description
    isArchived
    stargazerCount
    pushedAt
    defaultBranchRef { name }
    url
    latestRelease {
      tagName
      name
      publishedAt
      url
      description
    }
  }
}
"""

REPO_ACTIVITY = """
query($owner: String!, $name: String!, $since: DateTime!) {
  repository(owner: $owner, name: $name) {
    nameWithOwner
    pullRequests(first: 1, states: MERGED, orderBy: {field: UPDATED_AT, direction: DESC}) {
      totalCount
    }
    mergedRecent: pullRequests(
      first: 100
      states: MERGED
      orderBy: {field: UPDATED_AT, direction: DESC}
    ) {
      nodes { mergedAt }
    }
  }
}
"""

MERGED_PRS = """
query($owner: String!, $name: String!, $cursor: String) {
  repository(owner: $owner, name: $name) {
    pullRequests(
      first: 50
      after: $cursor
      states: MERGED
      orderBy: {field: UPDATED_AT, direction: DESC}
    ) {
      pageInfo { hasNextPage endCursor }
      nodes {
        databaseId
        number
        title
        body
        state
        url
        createdAt
        updatedAt
        mergedAt
        closedAt
        additions
        deletions
        changedFiles
        author { login }
        labels(first: 20) { nodes { name } }
        files(first: 100) {
          nodes { path additions deletions }
        }
      }
    }
  }
}
"""

OPEN_PRS = """
query($owner: String!, $name: String!, $cursor: String) {
  repository(owner: $owner, name: $name) {
    pullRequests(
      first: 50
      after: $cursor
      states: OPEN
      orderBy: {field: UPDATED_AT, direction: DESC}
    ) {
      pageInfo { hasNextPage endCursor }
      nodes {
        databaseId
        number
        title
        body
        state
        url
        createdAt
        updatedAt
        mergedAt
        closedAt
        additions
        deletions
        changedFiles
        author { login }
        labels(first: 20) { nodes { name } }
        reviews(first: 20, states: [APPROVED, CHANGES_REQUESTED, COMMENTED]) {
          nodes { author { login } state }
        }
        comments { totalCount }
        reviewThreads { totalCount }
        files(first: 100) {
          nodes { path additions deletions }
        }
      }
    }
  }
}
"""

REPO_ISSUES = """
query($owner: String!, $name: String!, $cursor: String) {
  repository(owner: $owner, name: $name) {
    issues(
      first: 50
      after: $cursor
      orderBy: {field: UPDATED_AT, direction: DESC}
      states: [OPEN, CLOSED]
    ) {
      pageInfo { hasNextPage endCursor }
      nodes {
        databaseId
        number
        title
        body
        state
        url
        createdAt
        updatedAt
        closedAt
        author { login }
        labels(first: 20) { nodes { name } }
        comments { totalCount }
        reactions { totalCount }
      }
    }
  }
}
"""

RELEASES = """
query($owner: String!, $name: String!, $cursor: String) {
  repository(owner: $owner, name: $name) {
    releases(first: 20, after: $cursor, orderBy: {field: CREATED_AT, direction: DESC}) {
      pageInfo { hasNextPage endCursor }
      nodes {
        tagName
        name
        description
        publishedAt
        url
        isDraft
        isPrerelease
      }
    }
  }
}
"""

TREE_ENTRIES = """
query($owner: String!, $name: String!, $expression: String!) {
  repository(owner: $owner, name: $name) {
    object(expression: $expression) {
      ... on Tree {
        entries {
          name
          type
          path
          object {
            ... on Blob { byteSize text }
          }
        }
      }
      ... on Blob {
        text
        byteSize
      }
    }
  }
}
"""

PATH_EXISTS = """
query($owner: String!, $name: String!, $expression: String!) {
  repository(owner: $owner, name: $name) {
    object(expression: $expression) {
      __typename
      ... on Tree { entries { name type } }
      ... on Blob { byteSize }
    }
  }
}
"""

CONTRIBUTOR_PRS = """
query($owner: String!, $name: String!, $cursor: String) {
  repository(owner: $owner, name: $name) {
    pullRequests(
      first: 50
      after: $cursor
      states: MERGED
      orderBy: {field: UPDATED_AT, direction: DESC}
    ) {
      pageInfo { hasNextPage endCursor }
      nodes {
        mergedAt
        author { login }
        reviews(first: 30, states: [APPROVED, CHANGES_REQUESTED, COMMENTED]) {
          nodes { author { login } }
        }
        files(first: 50) { nodes { path } }
      }
    }
  }
}
"""
