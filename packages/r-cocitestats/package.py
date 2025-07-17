# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCocitestats(RPackage):
    """Different test statistics based on co-citation.

    A collection of software tools for dealing with co-citation data.
    """

    bioc = "CoCiteStats"

    version("1.80.0", commit="7dbecb041af8e6f528320dab4824590b5d301c42")
    version("1.74.0", commit="5b7366fbfee85d04c6bbc0ea1f0076ac00ec0d5a")

    depends_on("r@2:", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
