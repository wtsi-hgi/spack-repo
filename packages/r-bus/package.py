# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBus(RPackage):
    """Gene network reconstruction

    This package can be used to compute associations among genes (gene-networks) or between genes and some external traits (i.e. clinical).
    """

    bioc = "BUS"

    version("1.64.0", commit="bdf79c3a9a27bd6ad0011e2dbf4fd4dee3703eb8")
    version("1.58.0", commit="9dcf16ab8b98421d17fc83d6bb9499932adbf04f")

    depends_on("r@2.3:", type=("build", "run"))
    depends_on("r-minet", type=("build", "run"))
    depends_on("r-infotheo", type=("build", "run"))
