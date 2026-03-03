# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTam(RPackage):
	"""Test Analysis Modules

	
    Includes marginal maximum likelihood estimation and joint maximum
    likelihood estimation for unidimensional and multidimensional 
    item response models. The package functionality covers the 
    Rasch model, 2PL model, 3PL model, generalized partial credit model, 
    multi-faceted Rasch model, nominal item response model, 
    structured latent class model, mixture distribution IRT models, 
    and located latent class models. Latent regression models and 
    plausible value imputation are also supported. For details see
    Adams, Wilson and Wang, 1997 <doi:10.1177/0146621697211001>,
    Adams, Wilson and Wu, 1997 <doi:10.3102/10769986022001047>,
    Formann, 1982 <doi:10.1002/bimj.4710240209>,
    Formann, 1992 <doi:10.1080/01621459.1992.10475229>.
	"""
	
	homepage = "http://www.edmeasurementsurveys.com/TAM/Tutorials/"
	cran = "TAM" 

	version("4.2-21", md5="69d3da387db835d829f63c954b6cb816")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-cdm@6.4.19:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
