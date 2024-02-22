# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMisaem(RPackage):
	"""Linear Regression and Logistic Regression with Missing
Covariates

	Estimate parameters of linear regression and logistic regression with missing covariates with missing data, perform model selection and prediction, using EM-type algorithms. Jiang W., Josse J., Lavielle M., TraumaBase Group (2020) <doi:10.1016/j.csda.2019.106907>.
	"""
	
	homepage = "https://github.com/julierennes/misaem"
	cran = "misaem" 

	version("1.0.1", md5="f16d582711f28cf3ae68cabe9ae30c1b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-norm", type=("build", "run"))
