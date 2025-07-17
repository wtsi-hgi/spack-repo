# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmdbquery(RPackage):
    """utilities for exploration of human metabolome database

    Define utilities for exploration of human metabolome database, including functions to retrieve specific metabolite entries and data snapshots with pairwise associations (metabolite-gene,-protein,-disease).
    """

    bioc = "hmdbQuery"

    version("1.28.0", commit="8324ee507d28027ec2dd5c5525b8bfe213b26667")
    version("1.22.0", commit="8e16e9493abfe8c2026156a9eeb052fff7079adb")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
