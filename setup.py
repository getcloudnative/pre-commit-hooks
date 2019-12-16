from setuptools import find_packages
from setuptools import setup


setup(
  name='pre_commit_hooks',
  description='Some useful hooks for https://pre-commit.com.',
  url='https://github.com/getcloudnative/pre-commit-hooks-terraform',
  version='1.0.0',

  author='Martin Etmajer',
  author_email='metmajer@getcloudnative.io',

  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
  ],

  packages=find_packages(),
  entry_points={
    'console_scripts': [
      'terraform_inputs_jenkins_pipeline_params = pre_commit_hooks.terraform_inputs_jenkins_pipeline_params:main',
    ],
  },
)
