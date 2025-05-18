import { ContentType } from '~lib/content/provider';

export const BASE_URL =
  process.env.NODE_ENV === 'development'
    ? 'http://localhost:3000'
    : 'https://kawka.me';

export const BLOG_PATH = '/blog';
export const BLOG_PATH_WITH_CATEGORY = (category: ContentType) =>
  `${BLOG_PATH}?content=${category}`;

export const GOOGLE_CODE_IN_ARTICLE_PATH = `${BLOG_PATH}/winning-google-code-in-2018`;

export const SOCIALS = {
  telegram: {
    url: 'https://t.me/letelete',
    handle: 'me/letelete',
  },
  mail: {
    url: 'akshaybapumore@gmail.com',
    handle: 'akshaybapumore@gmail.com',
  },
  linkedin: {
    url: 'https://www.linkedin.com/in/akshaymore10?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app',
    handle: 'in/akshaymore',
  },
  github: {
    url: 'https://github.com/AKSHAY-MORE10',
    handle: '@akshaymore',
  },
  twitter: {
    url: 'https://twitter.com/BrunoKawka',
    handle: '@brunokawka',
  },
  youtube: {
    url: 'https://www.youtube.com/@brunokawka',
    handle: '@brunokawka',
  },
  stackoverflow: {
    url: 'https://stackoverflow.com/users/8997321/bruno-kawka',
    handle: '@bruno-kawka',
  },
  reddit: {
    url: 'https://www.reddit.com/user/letelete0000/',
    handle: '@letelete0000',
  },
};

export const PORTFOLIO_GITHUB_REPOSITORY_URL =
  'https://github.com/letelete/letelete.github.io';
