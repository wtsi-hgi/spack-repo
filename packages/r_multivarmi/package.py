# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultivarmi(RPackage):
	"""Multiple Imputation for Multivariate Data

	Fully parametric Bayesian multiple imputation framework for massive multivariate data of different variable types as seen in Demirtas, H. (2017) <doi:10.1007/978-981-10-3307-0_8>.
	"""
	
	cran = "MultiVarMI" 

	version("1.0", md5="ab9855af3d24c18eee8e4fb40fc46014")

	depends_on("r-binordnonnor", type=("build", "run"))
	depends_on("r-corrtoolbox", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-norm", type=("build", "run"))
	depends_on("r-poisnonnor", type=("build", "run"))
