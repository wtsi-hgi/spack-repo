# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvanumt(RPackage):
    """NUMT detection from structural variant calls

    svaNUMT contains functions for detecting NUMT events from structural variant calls. It takes structural variant calls in GRanges of breakend notation and identifies NUMTs by nuclear-mitochondrial breakend junctions. The main function reports candidate NUMTs if there is a pair of valid insertion sites found on the nuclear genome within a certain distance threshold. The candidate NUMTs are reported by events.
    """

    bioc = "svaNUMT"

    version("1.14.0", commit="6bbbf6a697e0fcd41444ead04c8cb6d81b2c9da3")
    version("1.8.0", commit="fd711c3cbc925e3650dac6b8dc0a3b7defd49e1a")

    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-structuralvariantannotation", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r@4:", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
