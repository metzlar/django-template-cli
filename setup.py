from setuptools import setup # pragma: no cover 

setup(
  name='Django Template CLI',
  version='0.1',
  py_modules=['django_template_cli'],
  cmdclass={'upload':lambda x:None},
  install_requires=[
      'django',
  ],
)# pragma: no cover 
