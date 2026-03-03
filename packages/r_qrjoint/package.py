# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrjoint(RPackage):
	"""Joint Estimation in Linear Quantile Regression

	Joint estimation of quantile specific intercept and slope parameters in a linear regression setting.
	"""
	
	cran = "qrjoint" 

	version("2.0-9", md5="32347748f22764d8bd659a47975a87c0")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
