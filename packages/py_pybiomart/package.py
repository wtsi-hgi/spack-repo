# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPybiomart(PythonPackage):
    """A simple and pythonic biomart interface for Python."""

    homepage = "https://github.com/jrderuiter/pybiomart"
    pypi = "pybiomart/pybiomart-0.2.0.tar.gz"

    version("0.2.0", sha256="e9eac20db921820670c646d99725b0ee279e407379e5e8c3ec7245a07425d8fe")

    depends_on("py-future@0.15.2:", type=("build", "run"))
    depends_on("py-pandas@0.18.0:", type=("build", "run"))
    depends_on("py-requests@2.9.1:", type=("build", "run"))
    depends_on("py-requests-cache@0.4.12:", type=("build", "run"))
