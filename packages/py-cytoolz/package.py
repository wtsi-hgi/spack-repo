# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCytoolz(PythonPackage):
    """Cython implementation of the toolz package, which provides high performance utility functions for iterables, functions, and dictionaries."""

    homepage = "https://github.com/pytoolz/cytoolz"
    pypi = "cytoolz/cytoolz-0.12.3.tar.gz"

    version("0.12.3", sha256="4503dc59f4ced53a54643272c61dc305d1dbbfbd7d6bdf296948de9f34c3a282")

    depends_on("py-cython", type=("build", "run"))
