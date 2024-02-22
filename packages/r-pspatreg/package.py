# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPspatreg(RPackage):
	"""Spatial and Spatio-Temporal Semiparametric Regression Models
with Spatial Lags

	Estimation and inference of spatial and spatio-temporal 
    semiparametric models including spatial or spatio-temporal non-parametric 
    trends, parametric and non-parametric covariates and, possibly, a spatial 
    lag for the dependent variable and temporal correlation in the noise.
    The spatio-temporal trend can be decomposed in ANOVA way including main and 
    interaction functional terms. Use of SAP algorithm to estimate the spatial 
    or spatio-temporal trend and non-parametric covariates. The methodology of 
    these models can be found in next references
    Basile, R. et al. (2014), <doi:10.1016/j.jedc.2014.06.011>;
    Rodriguez-Alvarez, M.X. et al. (2015) <doi:10.1007/s11222-014-9464-2> and,
    particularly referred to the focus of the package, Minguez, R., 
    Basile, R. and Durban, M. (2020) <doi:10.1007/s10260-019-00492-8>.
	"""
	
	homepage = "https://github.com/rominsal/pspatreg"
	cran = "pspatreg" 

	version("1.1.2", md5="07eb4fc4ed6d715364c1fba8f6b7b257")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ameshousing@0.0.4:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-fields@14.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-mba@0.0.9:", type=("build", "run"))
	depends_on("r-mass@7.3.54:", type=("build", "run"))
	depends_on("r-minqa@1.2.5:", type=("build", "run"))
	depends_on("r-matrix@1.4.1:", type=("build", "run"))
	depends_on("r-numderiv@2016.8.1.1:", type=("build", "run"))
	depends_on("r-plm@2.6.2:", type=("build", "run"))
	depends_on("r-rdpack@2.4:", type=("build", "run"))
	depends_on("r-sf@1.0.8:", type=("build", "run"))
	depends_on("r-spatialreg@1.2.6:", type=("build", "run"))
	depends_on("r-spdep@1.2.7:", type=("build", "run"))
	depends_on("r-stringr@1.4.1:", type=("build", "run"))
