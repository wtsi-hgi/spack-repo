# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnota(RPackage):
    """ANalysis Of Translational Activity (ANOTA).

    Genome wide studies of translational control is emerging as a tool to study verious biological conditions. The output from such analysis is both the mRNA level (e.g. cytosolic mRNA level) and the levl of mRNA actively involved in translation (the actively translating mRNA level) for each mRNA. The standard analysis of such data strives towards identifying differential translational between two or more sample classes - i.e. differences in actively translated mRNA levels that are independent of underlying differences in cytosolic mRNA levels. This package allows for such analysis using partial variances and the random variance model. As 10s of thousands of mRNAs are analyzed in parallell the library performs a number of tests to assure that the data set is suitable for such analysis.
    """

    bioc = "anota"

    version("1.56.0", commit="ad0c0e281b743fd0e9b5d457b205a06753edb262")
    version("1.50.0", commit="b2d655d79deaffed32d64646db9e4d4bd6525fb9")

    depends_on("r-qvalue", type=("build", "run"))
    depends_on("r-multtest", type=("build", "run"))
