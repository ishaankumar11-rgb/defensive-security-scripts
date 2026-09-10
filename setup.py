from setuptools import setup, find_packages

setup(
    name="defensive-security-scripts",
    version="0.1.0",
    packages=find_packages(),
    py_modules=["port_scanner", "file_monitor"],
    install_requires=[
        # भविष्य में कोई बाहरी लाइब्रेरी चाहिए हो, तो यहाँ लिखें
    ],
    entry_points={
        "console_scripts": [
            "sec-scan=port_scanner:main_entry",
            "sec-monitor=file_monitor:main_entry",
        ],
    },
    author="Ishaan Kumar Giri",
    description="CLI tools for local security auditing and file integrity monitoring.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
