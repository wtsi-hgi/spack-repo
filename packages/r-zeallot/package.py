# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZeallot(RPackage):
    """Multiple, unpacking, and destructuring assignment in R

    Multiple, unpacking, and destructuring assignment. It's Python's
    tuple/list unpacking for R."""

    cran = "zeallot"

    version("0.1.0", sha256="6b008b843616a692e0e3906902fe414ebce338a54b6dad5cd863a5bd2cd03cb2")

    depends_on("r@3.5:", type=("build", "run"))
