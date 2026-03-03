# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEzodf(PythonPackage):
    """ezodf is a Python package to create new or open existing OpenDocument (ODF) files to extract, add, modify or delete document data."""

    homepage = "https://github.com/T0ha/ezodf"
    pypi = "ezodf/ezodf-0.3.2.tar.gz"

    version("0.3.2", sha256="000da534f689c6d55297a08f9e2ed7eada9810d194d31d164388162fb391122d")

    #depends_on("py-weakrefset", type=("build", "run"))
    depends_on("py-lxml", type=("build", "run"))
    depends_on("py-setuptools", type="build")
