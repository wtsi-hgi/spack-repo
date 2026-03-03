# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbnmadose(RPackage):
	"""Dose-Response MBNMA Models

	Fits Bayesian dose-response model-based network meta-analysis (MBNMA) 
    that incorporate multiple doses within an agent by modelling different dose-response functions, as
    described by Mawdsley et al. (2016) <doi:10.1002/psp4.12091>. 
    By modelling dose-response relationships this can connect networks of evidence that might
    otherwise be disconnected, and can improve precision on treatment estimates. Several common 
    dose-response functions are provided; others may be added by the user. Various characteristics
    and assumptions can be flexibly added to the models, such as shared class effects. The consistency 
    of direct and indirect evidence in the network can be assessed using unrelated mean effects models 
    and/or by node-splitting at the treatment level.
	"""
	
	homepage = "https://hugaped.github.io/MBNMAdose/"
	cran = "MBNMAdose" 

	version("0.4.2", md5="0db4b6c8d988adc762e24d3f3b933b3b")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-r2jags@0.5.7:", type=("build", "run"))
	depends_on("r-rjags@4.8:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-checkmate@1.8.5:", type=("build", "run"))
	depends_on("r-rdpack@0.11.0:", type=("build", "run"))
	depends_on("r-igraph@1.1.2:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("jags@4.3.0:", type=("build", "link", "run"))
