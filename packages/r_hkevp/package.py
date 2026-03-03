# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHkevp(RPackage):
	"""Spatial Extreme Value Analysis with the Hierarchical Model of
Reich and Shaby (2012)

	Several procedures for the hierarchical kernel extreme value process of Reich and Shaby (2012) <DOI:10.1214/12-AOAS591>, including simulation, estimation and spatial extrapolation. The spatial latent variable model <DOI:10.1214/11-STS376> is also included.
	"""
	
	cran = "hkevp" 

	version("1.1.5", md5="98191121d45434a3c7cb5250a57ea55b")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
