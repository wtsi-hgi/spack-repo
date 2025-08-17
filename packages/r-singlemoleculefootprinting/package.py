# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinglemoleculefootprinting(RPackage):
    """Analysis tools for Single Molecule Footprinting (SMF) data

    SingleMoleculeFootprinting is an R package providing functions to analyze Single Molecule Footprinting (SMF) data. Following the workflow exemplified in its vignette, the user will be able to perform basic data analysis of SMF data with minimal coding effort. Starting from an aligned bam file, we show how to perform quality controls over sequencing libraries, extract methylation information at the single molecule level accounting for the two possible kind of SMF experiments (single enzyme or double enzyme), classify single molecules based on their patterns of molecular occupancy, plot SMF information at a given genomic location
    """

    bioc = "SingleMoleculeFootprinting"

    version("2.2.0", commit="a14d84c9a8894f96a75a11feb6ac5bd1140e77f5")
    version("1.10.0", commit="44ae1a2b41153bb1391d228eecec53e29e0bdcb7")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-quasr", type=("build", "run"))
    # Additional CRAN/Bioconductor runtime dependencies inferred from DESCRIPTION
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-ggpointdensity", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-misctools", type=("build", "run"))
    depends_on("r-paralleldist", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-plyranges", type=("build", "run"))
    depends_on("r-viridis", type=("build", "run"))
