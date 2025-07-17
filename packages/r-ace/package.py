# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAce(RPackage):
    """Absolute Copy Number Estimation from Low-coverage Whole Genome Sequencing

    Uses segmented copy number data to estimate tumor cell percentage and produce copy number plots displaying absolute copy numbers.
    """

    homepage = "https://github.com/tgac-vumc/ACE"
    bioc = "ACE"

    version("1.26.0", commit="def9090148ca6996cdf0daacf021897d8653d8df")
    version("1.20.0", commit="1b2f96b83a1017c5a4ede76379311245d330eb3f")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-qdnaseq", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
