# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHanstat(RPackage):
	"""Package for Easy Interpretation of Statistical Methods

	A simple and time saving multiple linear regression function (OLS) with interpretation, optional bootstrapping, effect size calculation and all tested requirements.
	"""
	
	homepage = "https://github.com/KonradKrahl/HanStat"
	cran = "HanStat" 

	version("0.90.0", md5="2888c39e68e2cb23d034aab428af9e5f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-olsrr", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
