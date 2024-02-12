# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTyping(PythonPackage):
    """This is a backport of the standard library typing module to Python versions older than 3.5."""

    homepage = "https://docs.python.org/3/library/typing.html"
    pypi = "typing/typing-3.10.0.0.tar.gz"

    version("3.10.0.0", sha256="13b4ad211f54ddbf93e5901a9967b1e07720c1d1b78d596ac6a439641aa1b130")
