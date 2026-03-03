# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdmed(RPackage):
	"""Methods for Mediation Analysis with High-Dimensional Mediators

	A suite of functions for performing mediation
    analysis with high-dimensional mediators. In addition to centralizing code 
    from several existing packages for high-dimensional mediation analysis, we 
    provide organized, well-documented functions for a handle of methods 
    which, though programmed their original authors, have not previously been 
    formalized into R packages or been made presentable for public use. The 
    methods we include cover a broad array of approaches and objectives, and are
    described in detail by both our companion manuscript---"Methods for 
    Mediation Analysis with High-Dimensional DNA Methylation Data: Possible 
    Choices and Comparison"---and the original publications that proposed them. 
    The specific methods offered by our package include the Bayesian sparse 
    linear mixed model (BSLMM) by Song et al. (2019); high-dimensional mediation
    analysis (HDMA) by Gao et al. (2019); high-dimensional multivariate 
    mediation (HDMM) by Chén et al. (2018); high-dimensional linear mediation 
    analysis (HILMA) by Zhou et al. (2020); high-dimensional mediation analysis
    (HIMA) by Zhang et al. (2016); latent variable mediation analysis (LVMA) by 
    Derkach et al. (2019); mediation by fixed-effect model (MedFix) by 
    Zhang (2021); pathway LASSO by Zhao & Luo (2022); principal component 
    mediation analysis (PCMA) by Huang & Pan (2016); and sparse principal 
    component mediation analysis (SPCMA) by Zhao et al. (2020). Citations for 
    the corresponding papers can be found in their respective functions.
	"""
	
	cran = "hdmed" 

	version("1.0.0", md5="18d94aefa7a443d5bb499920b6c59ef4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bama@1.3:", type=("build", "run"))
	depends_on("r-foreach@1.5.2:", type=("build", "run"))
	depends_on("r-freebird@1:", type=("build", "run"))
	depends_on("r-gcdnet@1.0.6:", type=("build", "run"))
	depends_on("r-genlasso@1.6.1:", type=("build", "run"))
	depends_on("r-hdi@0.1.9:", type=("build", "run"))
	depends_on("r-iterators@1.0.14:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mediation@4.5:", type=("build", "run"))
	depends_on("r-ncvreg@3.13:", type=("build", "run"))
