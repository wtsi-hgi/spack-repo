# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaseqsamplesizedata(RPackage):
    """RnaSeqSampleSizeData

    RnaSeqSampleSizeData package provides the read counts and dispersion distribution from real RNA-seq experiments. It can be used by RnaSeqSampleSize package to estimate sample size and power for RNA-seq experiment design.
    """

    bioc = "RnaSeqSampleSizeData"

    version("1.40.0", commit="5acfecf6911e2a13a09757aeb7ed2a17efd2021d")
    version("1.34.0", commit="18c0ea15abf16a037c5d23f777bd0be0176108d7")

    depends_on("r-edger", type=("build", "run"))
    depends_on("r@2.10:", type=("build", "run"))
