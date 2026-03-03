# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPenppml(RPackage):
	"""Penalized Poisson Pseudo Maximum Likelihood Regression

	A set of tools that enables efficient estimation of penalized 
    Poisson Pseudo Maximum Likelihood regressions, using lasso or ridge penalties, for models 
    that feature one or more sets of high-dimensional fixed effects. The methodology is based on 
    Breinlich, Corradi, Rocha, Ruta, Santos Silva, and Zylkin (2021) <http://hdl.handle.net/10986/35451> 
    and takes advantage of the method of alternating projections of Gaure (2013) 
    <doi:10.1016/j.csda.2013.03.024> for dealing with HDFE, as well as 
    the coordinate descent algorithm of Friedman, Hastie and Tibshirani (2010) 
    <doi:10.18637/jss.v033.i01> for fitting lasso regressions. The package is also able to carry out 
    cross-validation and to implement the plugin lasso of Belloni, Chernozhukov, Hansen and Kozbur (2016) 
    <doi:10.1080/07350015.2015.1102733>.
	"""
	
	homepage = "https://github.com/tomzylkin/penppml"
	cran = "penppml" 

	version("0.2.3", md5="35ef7a09655e84b56ef969d22f71f8f7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-fixest", type=("build", "run"))
	depends_on("r-collapse", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
