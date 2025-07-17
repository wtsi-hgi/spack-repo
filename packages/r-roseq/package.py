# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoseq(RPackage):
    """Modeling expression ranks for noise-tolerant differential expression analysis of scRNA-Seq data

    ROSeq - A rank based approach to modeling gene expression with filtered and normalized read count matrix. ROSeq takes filtered and normalized read matrix and cell-annotation/condition as input and determines the differentially expressed genes between the contrasting groups of single cells. One of the input parameters is the number of cores to be used.
    """

    homepage = "https://github.com/krishan57gupta/ROSeq"
    bioc = "ROSeq"

    version("1.20.0", commit="a086429cde602b7db39a9315f71f0419d0f86565")
    version("1.14.0", commit="356733ae00114c2e2251509ba8bf6612ac26d1cf")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-pbmcapply", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
