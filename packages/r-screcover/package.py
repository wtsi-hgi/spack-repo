# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrecover(RPackage):
    """scRecover for imputation of single-cell RNA-seq data

    scRecover is an R package for imputation of single-cell RNA-seq (scRNA-seq) data. It will detect and impute dropout values in a scRNA-seq raw read counts matrix while keeping the real zeros unchanged, since there are both dropout zeros and real zeros in scRNA-seq data. By combination with scImpute, SAVER and MAGIC, scRecover not only detects dropout and real zeros at higher accuracy, but also improve the downstream clustering and visualization results.
    """

    homepage = "https://miaozhun.github.io/scRecover"
    bioc = "scRecover"

    version("1.24.0", commit="48612ddea5d0319de903121435d9d5e83c777f54")
    version("1.18.0", commit="75e8fa3a7fb326375338498b1cbfc87faacd2ec8")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-penalized", type=("build", "run"))
    depends_on("r-kernlab", type=("build", "run"))
    depends_on("r-rsvd", type=("build", "run"))
    depends_on("r-matrix@1.2.14:", type=("build", "run"))
    depends_on("r-mass@7.3.45:", type=("build", "run"))
    depends_on("r-pscl@1.4.9:", type=("build", "run"))
    depends_on("r-bbmle@1.0.18:", type=("build", "run"))
    depends_on("r-gamlss@4.4.0:", type=("build", "run"))
    depends_on("r-preseqr@4:", type=("build", "run"))
    depends_on("r-saver@1.1.1:", type=("build", "run"))
    depends_on("r-biocparallel@1.12:", type=("build", "run"))
