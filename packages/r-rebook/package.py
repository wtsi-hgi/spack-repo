# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRebook(RPackage):
    """Re-using Content in Bioconductor Books

    Provides utilities to re-use content across chapters of a Bioconductor book. This is mostly based on functionality developed while writing the OSCA book, but generalized for potential use in other large books with heavy compute. Also contains some functions to assist book deployment.
    """

    bioc = "rebook"

    version("1.18.0", commit="0f0347f9959475c0b6c9f80cf5e112606b901c3d")
    version("1.12.0", commit="bfb9a3ff451244963cb77e523ecfbbc9ece3ea2a")

    depends_on("r-knitr@1.32:", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-codedepends", type=("build", "run"))
    depends_on("r-dir-expiry", type=("build", "run"))
    depends_on("r-filelock", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
