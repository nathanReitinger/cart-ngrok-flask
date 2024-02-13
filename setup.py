import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cart-flask-ngrok",
    version="0.0.1",
    author="Nathan Reitinger",
    description="An offshoot of flask-ngrok for demo Flask apps using ngrok.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    keywords='flask ngrok CART',
    install_requires=['Flask>=0.8', 'requests'],
    py_modules=['cart_flask_ngrok']
)
