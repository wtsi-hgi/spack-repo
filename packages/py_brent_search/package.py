# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBrentSearch(PythonPackage):
    """Brent's method for univariate function optimization."""

    homepage = "https://github.com/limix/brent-search"
    pypi = "brent-search/brent-search-2.0.1.tar.gz"

    version("2.0.1", sha256="6153e7541dc19ded662c7149fdc573d9367c41438d8c0e5dbcc751120b3ecb55")

    depends_on("py-numpy@1.14.5:", type=("build", "run"))
    depends_on("py-pytest@6.0.0:", type=("build", "run"))
