# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpsur(RPackage):
	"""Spatial Seemingly Unrelated Regression Models

	A collection of functions to test and estimate Seemingly 
    Unrelated Regression (usually called SUR) models, with spatial structure, by maximum 
    likelihood and three-stage least squares. The package estimates the 
    most common spatial specifications, that is, SUR with Spatial Lag of 
    X regressors (called SUR-SLX), SUR with Spatial Lag Model (called SUR-SLM), 
    SUR with Spatial Error Model (called SUR-SEM), SUR with Spatial Durbin Model (called SUR-SDM), 
    SUR with Spatial Durbin Error Model (called SUR-SDEM), 
    SUR with Spatial Autoregressive terms and Spatial Autoregressive 
    Disturbances (called SUR-SARAR), SUR-SARAR with Spatial Lag of X 
    regressors (called SUR-GNM) and SUR with Spatially Independent Model (called SUR-SIM).
    The methodology of these models can be found in next references 
    Minguez, R., Lopez, F.A., and Mur, J. (2022) <doi:10.18637/jss.v104.i11>
    Mur, J., Lopez, F.A., and Herrera, M. (2010) <doi:10.1080/17421772.2010.516443> 
    Lopez, F.A., Mur, J., and Angulo, A. (2014) <doi:10.1007/s00168-014-0624-2>.
	"""
	
	homepage = "https://CRAN.R-project.org/package=spsur"
	cran = "spsur" 

	version("1.0.2.5", md5="4d3ef72a9db9e5573a498949eaf1779c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-formula@1.2.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-gmodels@2.18.1:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-mass@7.3.56:", type=("build", "run"))
	depends_on("r-matrix@1.4.1:", type=("build", "run"))
	depends_on("r-minqa@1.2.4:", type=("build", "run"))
	depends_on("r-numderiv@2016.8.1.1:", type=("build", "run"))
	depends_on("r-rdpack@2.4:", type=("build", "run"))
	depends_on("r-rlang@1.0.4:", type=("build", "run"))
	depends_on("r-sparsemvn@0.2.2:", type=("build", "run"))
	depends_on("r-spatialreg@1.2.5:", type=("build", "run"))
	depends_on("r-spdep@1.2.5:", type=("build", "run"))
	depends_on("r-sphet@2:", type=("build", "run"))
