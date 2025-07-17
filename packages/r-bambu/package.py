# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBambu(RPackage):
    """Context-Aware Transcript Quantification from Long Read RNA-Seq data

    bambu is a R package for multi-sample transcript discovery and quantification using long read RNA-Seq data. You can use bambu after read alignment to obtain expression estimates for known and novel transcripts and genes. The output from bambu can directly be used for visualisation and downstream analysis such as differential gene expression or transcript usage.
    """

    homepage = "https://github.com/GoekeLab/bambu"
    bioc = "bambu"

    version("3.10.1", commit="6647ed583046f5405efdfdb4f95c90ecede03bca")
    version("3.6.0", md5="6dea2d02b1715b82c09c0b1eed6a2adb")
    version("3.4.0", md5="900e0e67c251f12989154113c54d2b32")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-summarizedexperiment@1.1.6:", type=("build", "run"))
    depends_on("r-s4vectors@0.22.1:", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-xgboost", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
