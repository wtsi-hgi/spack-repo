# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RMclogit(RPackage):
	"""Multinomial Logit Models, with or without Random Effects or
Overdispersion

	Provides estimators for multinomial logit models in their
    conditional logit and baseline logit variants, with or without random effects,
    with or without overdispersion. 
    Random effects models are estimated using the PQL technique (based on a Laplace approximation)
    or the MQL technique (based on a Solomon-Cox approximation). Estimates should be treated
    with caution if the group sizes are small.
	"""
	
	homepage = "http://mclogit.elff.eu"
	cran = "mclogit" 

	version("0.9.6", md5="fde8195c54f7096ebf8071b67b44ddab")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-memisc", type=("build", "run"))
