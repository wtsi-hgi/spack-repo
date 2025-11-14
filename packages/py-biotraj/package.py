# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBiotraj(PythonPackage):
    """Basic trajectory file format functionality for Biotite; forked from MDTraj"""
    
    homepage = "https://www.biotite-python.org"
    pypi = "biotraj/biotraj-1.2.2.tar.gz" 

    version("0.1", sha256="064bf4a81b60d7181658d2a0604a8374c213988f5a9e55da1206f5712d036fb1")
    version("1.1.0", sha256="77f6f93bf91965973ff5645c19f5825977ecb3fdee43e82c5b39eaf4a568a215")
    version("1.2.0", sha256="c96bf24bfd169b5f4ad43a0699f90c7e801ef82ab6ca7016511d8f636bb2b286")
    version("1.2.1", sha256="4d7ad33ad940dbcfb3c2bd228a18f33f88e04657786a9562173b58dc2dd05349")
    version("1.2.2", sha256="4bcba92101ed50f369cc1487fb5dfcfe1d8402ad47adaa9232b080553271663a")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-cython@0.29:", type="build")
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-numpy@1.25:", type=("build", "run"))
    depends_on("py-scipy@1.13:", type=("build", "run"))
