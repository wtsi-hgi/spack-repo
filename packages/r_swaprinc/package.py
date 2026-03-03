# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwaprinc(RPackage):
	"""Swap Principal Components into Regression Models

	Obtaining accurate and stable estimates of regression coefficients
    can be challenging when the suggested statistical model has issues related to
    multicollinearity, convergence, or overfitting. One solution is to use
    principal component analysis (PCA) results in the regression, as discussed in
    Chan and Park (2005) <doi:10.1080/01446190500039812>. The swaprinc() package
    streamlines comparisons between a raw regression model with the full set of
    raw independent variables and a principal component regression model where
    principal components are estimated on a subset of the independent variables,
    then swapped into the regression model in place of those variables. The
    swaprinc() function compares one raw regression model to one principal
    component regression model, while the compswap() function compares one raw
    regression model to many principal component regression models. Package
    functions include parameters to center, scale, and undo centering and scaling,
    as described by Harvey and Hansen (2022)
    <https://cran.r-project.org/package=LearnPCA/vignettes/Vig_03_Step_By_Step_PCA.pdf>.
    Additionally, the package supports using Gifi methods to extract principal
    components from categorical variables, as outlined by Rossiter (2021)
    <https://www.css.cornell.edu/faculty/dgr2/_static/files/R_html/NonlinearPCA.html#2_Package>.
	"""
	
	homepage = "https://github.com/mncube/swaprinc"
	cran = "swaprinc" 

	version("1.0.1", md5="3a1f0070e30937b6b3ce3327b26282db")

	depends_on("r-broom", type=("build", "run"))
	depends_on("r-broom-mixed", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gifi", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
