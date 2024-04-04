# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class PyGetcontacts(PythonPackage):
    """Application for efficiently computing non-covalent contact networks in molecular structures and MD simulations."""

    homepage = "https://github.com/getcontacts/getcontacts"
    git = "https://github.com/getcontacts/getcontacts"

    version("1.0", commit="da14deb")

    depends_on("python@3.9.9", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-vmd", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("expat", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-pytest", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))

    def patch(self):
        mkdir("Getcontacts")
        for file in ["get_contact_bridges.py",
                     "get_contact_fingerprints.py",
                     "get_contact_flare.py",
                     "get_contact_frequencies.py",
                     "get_contact_singleframe.py",
                     "get_contact_ticc.py",
                     "get_contact_trace.py",
                     "get_dynamic_contacts.py",
                     "get_resilabels.py",
                     "get_static_contacts.py"]:
            move(file, "Getcontacts/")

        with open("setup.py", "w") as fh:
            fh.write("""
import sys
from setuptools import setup, find_packages
                     
setup(
    name='Getcontacts',
    version='1.0',
    packages=find_packages(),

    python_requires='>=3.6',
    install_requires=[
        'requests',
        'numpy',
        'scipy',
        'matplotlib',
        'scikit-learn',
        'pandas',
        'seaborn',
        'vmd'],
                     
    scripts=[
        'Getcontacts/get_dynamic_contacts.py', 
        'Getcontacts/get_static_contacts.py',
        'Getcontacts/get_contact_bridges.py',
        'Getcontacts/get_contact_fingerprints.py',
        'Getcontacts/get_contact_flare.py',
        'Getcontacts/get_contact_frequencies.py',
        'Getcontacts/get_contact_singleframe.py',
        'Getcontacts/get_contact_ticc.py',
        'Getcontacts/get_contact_trace.py',
        'Getcontacts/get_resilabels.py'],
)""")