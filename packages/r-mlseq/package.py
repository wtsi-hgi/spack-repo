# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlseq(RPackage):
    """Machine Learning Interface for RNA-Seq Data

    This package applies several machine learning methods, including SVM, bagSVM, Random Forest and CART to RNA-Seq data.
    """

    bioc = "MLSeq"

    version("2.26.0", commit="f150f3e00776196e28ed584165e3952294110a0b")
    version("2.20.0", commit="d41d6a4effc49e7d2de35bbbd026ca8e52186c58")

    depends_on("r-caret", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-venndiagram", type=("build", "run"))
    depends_on("r-pamr", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-sseq", type=("build", "run"))
    depends_on("r-xtable", type=("build", "run"))
