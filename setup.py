from setuptools import setup

setup(
    name='tt_log_filter',
    description='TipTap log filtering library.',
    long_description=(
        '%s\n\n%s' % (
            open('README.md').read(),
            open('CHANGELOG.md').read()
        )
    ),
    version=open('VERSION').read().strip(),
    author='TipTap',
    install_requires=[],
    packages=['tt_log_filter']
)
