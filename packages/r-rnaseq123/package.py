# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaseq123(RPackage):
    """RNA-seq analysis is easy as 1-2-3 with limma, Glimma and edgeR

    R package that supports the F1000Research workflow article on RNA-seq analysis using limma, Glimma and edgeR by Law et al. (2016).
    """

    homepage = "https://f1000research.com/articles/5-1408/v3"
    bioc = "RNAseq123"

    version("1.32.0", commit="25984b20bfe8d7b9b45a6f59d3031a65b98d202f")
    version("1.26.0", commit="40f3611cbe2af77ab0aabc80abe15aaebe3e3dee")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-glimma@1.1.9:", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-mus-musculus", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-teachingdemos", type=("build", "run"))
    depends_on("r-statmod", type=("build", "run"))
    depends_on("r-biocworkflowtools", type=("build", "run"))
