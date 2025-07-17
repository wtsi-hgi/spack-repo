# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtpca(RPackage):
    """Thermal proximity co-aggregation with R

    R package for performing thermal proximity co-aggregation analysis with thermal proteome profiling datasets to analyse protein complex assembly and (differential) protein-protein interactions across conditions.
    """

    bioc = "Rtpca"

    version("1.18.0", commit="9688ca622c31a019c88d61609405e92b7818ad89")
    version("1.12.0", commit="9116e935321cb8abca734131d38a43a776b267c7")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-proc", type=("build", "run"))
    depends_on("r-fdrtool", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
