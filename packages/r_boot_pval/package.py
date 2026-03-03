# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootPval(RPackage):
	"""Bootstrap p-Values

	Computation of bootstrap p-values through inversion of confidence intervals, including convenience functions for regression models.
	"""
	
	cran = "boot.pval" 

	version("0.5", md5="d13f774df261623c36a17249f8c27cd8")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
