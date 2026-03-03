# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdmb(RPackage):
	"""Model Based Treatment of Missing Data

	
    Contains model-based treatment of missing data for regression 
    models with missing values in covariates or the dependent 
    variable using maximum likelihood or Bayesian estimation 
    (Ibrahim et al., 2005; <doi:10.1198/016214504000001844>;
    Luedtke, Robitzsch, & West, 2020a, 2020b;
    <doi:10.1080/00273171.2019.1640104><doi:10.1037/met0000233>).
    The regression model can be nonlinear (e.g., interaction 
    effects, quadratic effects or B-spline functions). 
    Multilevel models with missing data in predictors are
    available for Bayesian estimation. Substantive-model compatible 
    multiple imputation can be also conducted.
	"""
	
	homepage = "https://github.com/alexanderrobitzsch/mdmb"
	cran = "mdmb" 

	version("1.8-7", md5="55fde9d1facf3c2e3264d5e9ef749c2f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-cdm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-miceadds", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sirt", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
