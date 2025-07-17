# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuitor(RPackage):
    """Selecting the number of mutational signatures through cross-validation

    An unsupervised cross-validation method to select the optimal number of mutational signatures. A data set of mutational counts is split into training and validation data.Signatures are estimated in the training data and then used to predict the mutations in the validation data.
    """

    bioc = "SUITOR"

    version("1.10.0", commit="283c6e28cf0f986d0d228a67517c723f850596b2")
    version("1.4.0", commit="f2a596a57810e7845a7e85bcb1beaaa041a0e4e5")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
