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

    # CRAN re-rolled archives can change checksums; update to fetched one
    version("0.1.0", sha256="439f1213c97c8ddef9a1e1499bdf81c2940859f78b76bc86ba476cebd88ba1e9")

    depends_on("r@3.5:", type=("build", "run"))
