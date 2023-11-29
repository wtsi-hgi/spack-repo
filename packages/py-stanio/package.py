# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyStanio(PythonPackage):
    """A set of functions for data-wrangling in the formats used by the Stan probabalistic programming language."""

    homepage = "https://mc-stan.org/"
    pypi = "stanio/stanio-0.4.0.tar.gz"

    version("0.4.0", sha256="8b586ac14b35cde1aad188dbf85824515c6842dc951a2b411dd138fb5c35fc9f")

    depends_on("py-setuptools")
