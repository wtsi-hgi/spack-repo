# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialrf(RPackage):
	"""Easy Spatial Modeling with Random Forest

	Automatic generation and selection of spatial predictors for spatial regression with Random Forest. Spatial predictors are surrogates of variables driving the spatial structure of a response variable. The package offers two methods to generate spatial predictors from a distance matrix among training cases: 1) Moran's Eigenvector Maps (MEMs; Dray, Legendre, and Peres-Neto 2006 <DOI:10.1016/j.ecolmodel.2006.02.015>): computed as the eigenvectors of a weighted matrix of distances; 2) RFsp (Hengl et al. <DOI:10.7717/peerj.5518>): columns of the distance matrix used as spatial predictors. Spatial predictors help minimize the spatial autocorrelation of the model residuals and facilitate an honest assessment of the importance scores of the non-spatial predictors. Additionally, functions to reduce multicollinearity, identify relevant variable interactions, tune random forest hyperparameters, assess model transferability via spatial cross-validation, and explore model results via partial dependence curves and interaction surfaces are included in the package. The modelling functions are built around the highly efficient 'ranger' package (Wright and Ziegler 2017 <DOI:10.18637/jss.v077.i01>).  
	"""
	
	homepage = "https://blasbenito.github.io/spatialRF/"
	cran = "spatialRF" 

	version("1.1.4", md5="8476a9e331464662f6a149b2b44173db")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-huxtable", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
