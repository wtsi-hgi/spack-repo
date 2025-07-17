# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVplotr(RPackage):
    """Set of tools to make V-plots and compute footprint profiles

    The pattern of digestion and protection from DNA nucleases such as DNAse I, micrococcal nuclease, and Tn5 transposase can be used to infer the location of associated proteins. This package contains useful functions to analyze patterns of paired-end sequencing fragment density. VplotR facilitates the generation of V-plots and footprint profiles over single or aggregated genomic loci of interest.
    """

    homepage = "https://github.com/js2264/VplotR"
    bioc = "VplotR"

    version("1.18.0", commit="2fddd4784c8d56aecd98e47adfe6302b163cf659")
    version("1.12.1", commit="3f96ff515792657644dce8fe3ea5d42bdfd49da4")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-zoo", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
