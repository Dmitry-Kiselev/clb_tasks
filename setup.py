from setuptools import setup

setup(name='cluster_tasks',
      version='0.1',
      description='package with simple tasks',
      author='Dmitry Kiselev',
      author_email='kdem27@gmail.com',
      license='MIT',
      packages=['cluster_tasks'],
      install_requires=[
          'celery',
      ],
      zip_safe=False)