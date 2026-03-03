# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarreg(RPackage):
	"""Semi-Parametric Variance Regression

	Methods for fitting semi-parametric mean and variance models, with normal or censored data. Extended to allow a regression in the location, scale and shape parameters, and further for multiple regression in each.
	"""
	
	cran = "VarReg" 

	version("2.0", md5="1887f7fed4f3349fcd9776fb94fd0039")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
