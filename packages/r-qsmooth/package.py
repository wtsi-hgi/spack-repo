# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQsmooth(RPackage):
    """Smooth quantile normalization

    Smooth quantile normalization is a generalization of quantile normalization, which is average of the two types of assumptions about the data generation process: quantile normalization and quantile normalization between groups.
    """

    bioc = "qsmooth"

    version("1.24.0", commit="23f418446d46fcf3550b9d1f034028c3526d3539")
    version("1.18.0", commit="c82730e429499e7ae420babe6e4e49497eb8d407")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-sva", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
