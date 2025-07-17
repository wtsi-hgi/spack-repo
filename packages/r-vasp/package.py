# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVasp(RPackage):
    """Quantification and Visualization of Variations of Splicing in Population

    Discovery of genome-wide variable alternative splicing events from short-read RNA-seq data and visualizations of gene splicing information for publication-quality multi-panel figures in a population. (Warning: The visualizing function is removed due to the dependent package Sushi deprecated. If you want to use it, please change back to an older version.)
    """

    homepage = "https://github.com/yuhuihui2011/VaSP"
    bioc = "VaSP"

    version("1.20.0", commit="fbf6c55f0fc03697841d5c892a60414451259154")
    version("1.14.0", commit="93668068fbe73084ce26b138e4d256d6020cee85")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-ballgown", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
