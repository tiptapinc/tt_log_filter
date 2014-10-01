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
    package_dir={'tt_log_filter': 'src'},
    packages=['tt_log_filter']
)
