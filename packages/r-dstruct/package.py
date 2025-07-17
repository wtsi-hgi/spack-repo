# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDstruct(RPackage):
    """Identifying differentially reactive regions from RNA structurome profiling data

    dStruct identifies differentially reactive regions from RNA structurome profiling data. dStruct is compatible with a broad range of structurome profiling technologies, e.g., SHAPE-MaP, DMS-MaPseq, Structure-Seq, SHAPE-Seq, etc. See Choudhary et al., Genome Biology, 2019 for the underlying method.
    """

    homepage = "https://github.com/dataMaster-Kris/dStruct"
    bioc = "dStruct"

    version("1.14.0", commit="524856f348b33eedaf3931a9f20908849a7f1d3e")
    version("1.8.0", commit="10bfcdb6e4d567f492056a8a4e2e28fe459e20fa")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-zoo", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
