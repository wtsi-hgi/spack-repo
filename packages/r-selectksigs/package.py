# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelectksigs(RPackage):
    """Selecting the number of mutational signatures using a perplexity-based measure and cross-validation

    A package to suggest the number of mutational signatures in a collection of somatic mutations using calculating the cross-validated perplexity score.
    """

    homepage = "https://github.com/USCbiostats/selectKSigs"
    bioc = "selectKSigs"

    version("1.20.0", commit="674fc2ba038bd69fe2d251974c52d3550bcea2b1")
    version("1.14.0", commit="d94052166954e29b8ed55bd30d0b22faa8637149")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-hilda", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
