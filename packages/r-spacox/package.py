# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpacox(RPackage):
    """A semiparametric empirical SPA approach based on a Cox regression model fitting (SPACox), that is scalable for a genome-wide single-variant survival analysis in large cohorts"""

    homepage = "https://github.com/WenjianBI/SPACox/"
    git = "https://github.com/WenjianBI/SPACox.git"

    version("2021-03-02", commit="a20203497132c93ff4ec2e9e70592c0883a749bc")

    depends_on("r-seqminer", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
