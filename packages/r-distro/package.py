# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RDistro(RPackage):
    """In order to provide unified access to Linux distribution details in R, this package wraps the various files and commands that may exist on a system."""

    cran = "distro"

    version("0.1.0", sha256="4fd8a62c56c63d35dc72ed64d526e4eed581d42044d65a8e1909f60ee5ac680d")
    depends_on("r-testthat", type=("build", "run"))
