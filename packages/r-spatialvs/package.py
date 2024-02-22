# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialvs(RPackage):
	"""Spatial Variable Selection

	Perform variable selection for the spatial Poisson regression model under the adaptive elastic net penalty. Spatial count data with covariates is the input. We use a spatial Poisson regression model to link the spatial counts and covariates. For maximization of the likelihood under adaptive elastic net penalty, we implemented the penalized quasi-likelihood (PQL) and the approximate penalized loglikelihood (APL) methods. The proposed methods can automatically select important covariates, while adjusting for possible spatial correlations among the responses. More details are available in Xie et al. (2018, <arXiv:1809.06418>). The package also contains the Lyme disease dataset, which consists of the disease case data from 2006 to 2011, and demographic data and land cover data in Virginia. The Lyme disease case data were collected by the Virginia Department of Health. The demographic data (e.g., population density, median income, and average age) are from the 2010 census. Land cover data were obtained from the Multi-Resolution Land Cover Consortium for 2006.
	"""
	
	cran = "SpatialVS" 

	version("1.1", md5="df1e191557f49d13eeb7c9677c283992")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
