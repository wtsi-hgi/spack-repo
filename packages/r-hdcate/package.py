# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdcate(RPackage):
	"""Estimation of Conditional Average Treatment Effects with
High-Dimensional Data

	A two-step double-robust method to estimate the conditional average treatment effects (CATE) with potentially high-dimensional covariate(s). In the first stage, the nuisance functions necessary for identifying CATE are estimated by machine learning methods, allowing the number of covariates to be comparable to or larger than the sample size. The second stage consists of a low-dimensional local linear regression, reducing CATE to a function of the covariate(s) of interest. The CATE estimator implemented in this package not only allows for high-dimensional data, but also has the “double robustness” property: either the model for the propensity score or the models for the conditional means of the potential outcomes are allowed to be misspecified (but not both). This package is based on the paper by Fan et al., "Estimation of Conditional Average Treatment Effects With High-Dimensional Data" (2022), Journal of Business & Economic Statistics <doi:10.1080/07350015.2020.1811102>.
	"""
	
	cran = "hdcate" 

	version("0.1.0", md5="835a5b4c65a81b13fa4f1de6f0f66e1f")

	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-hdm", type=("build", "run"))
	depends_on("r-locpol", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
