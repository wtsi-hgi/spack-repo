# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNsm3(RPackage):
	"""Functions and Datasets to Accompany Hollander, Wolfe, and
Chicken - Nonparametric Statistical Methods, Third Edition

	Designed to replace the tables which were in the back of the first two editions of Hollander and Wolfe - Nonparametric Statistical Methods.  Exact procedures are performed when computationally possible.  Monte Carlo and Asymptotic procedures are performed otherwise.  For those procedures included in the base packages, our code simply provides a wrapper to standardize the output with the other procedures in the package.
	"""
	
	cran = "NSM3" 

	version("1.18", md5="0bf2fb764796dd3ececbe8f207ad2520", url="https://cran.r-project.org/src/contrib/NSM3_1.18.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-agricolae", type=("build", "run"))
	depends_on("r-ash", type=("build", "run"))
	depends_on("r-binom", type=("build", "run"))
	depends_on("r-bsda", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-fancova", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-km-ci", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-rfit", type=("build", "run"))
	depends_on("r-suppdists", type=("build", "run"))
	depends_on("r-waveslim", type=("build", "run"))
