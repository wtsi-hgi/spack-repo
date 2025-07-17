# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCma(RPackage):
    """Synthesis of microarray-based classification

    This package provides a comprehensive collection of various microarray-based classification algorithms both from Machine Learning and Statistics. Variable Selection, Hyperparameter tuning, Evaluation and Comparison can be performed combined or stepwise in a user-friendly environment.
    """

    bioc = "CMA"

    version("1.66.0", commit="59b96f7758d5d13a7cb8b415879d5b4e55e54686")
    version("1.60.0", commit="21f98b08c39cc81e3dfa98cc68b25a06607edde1")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
