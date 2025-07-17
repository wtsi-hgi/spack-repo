# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicozone(RPackage):
    """Delineate outstanding genomic zones of differential gene activity

    The package clusters gene activity along chromosome into zones, detects differential zones as outstanding, and visualizes maps of outstanding zones across the genome. It enables characterization of effects on multiple genes within adaptive genomic neighborhoods, which could arise from genome reorganization, structural variation, or epigenome alteration. It guarantees cluster optimality, linear runtime to sample size, and reproducibility. One can apply it on genome-wide activity measurements such as copy number, transcriptomic, proteomic, and methylation data.
    """

    bioc = "GenomicOZone"

    version("1.22.0", commit="5664c07570d701a6312f71607eb1552dd309ddbd")
    version("1.16.0", commit="7e7361a1075bef1e58c94747ca64a88b7255df8d")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-ckmeans-1d-dp@4.3:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-lsr", type=("build", "run"))
    depends_on("r-ggbio", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-rdpack", type=("build", "run"))
