# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHilda(RPackage):
    """Conducting statistical inference on comparing the mutational exposures of mutational signatures by using hierarchical latent Dirichlet allocation

    A package built under the Bayesian framework of applying hierarchical latent Dirichlet allocation. It statistically tests whether the mutational exposures of mutational signatures (Shiraishi-model signatures) are different between two groups. The package also provides inference and visualization.
    """

    homepage = "https://github.com/USCbiostats/HiLDA"
    bioc = "HiLDA"

    version("1.22.0", commit="b2276ffe8523e6e06fde77997f44e01c9c9211e8")
    version("1.16.0", commit="b74fe6d2208d7034471526caebb2ab1ce6c83f28")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-r2jags", type=("build", "run"))
    depends_on("r-abind", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-forcats", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-xvector", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("jags@4.0.0:", type=("build", "link", "run"))
