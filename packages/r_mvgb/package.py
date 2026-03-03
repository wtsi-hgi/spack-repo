# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvgb(RPackage):
	"""Multivariate Probabilities of Scale Mixtures of Multivariate
Normal Distributions via the Genz and Bretz (2002) QRSVN Method

	Generates multivariate subgaussian stable probabilities using the QRSVN
    algorithm as detailed in Genz and Bretz (2002) <DOI:10.1198/106186002394>
    but by sampling positive stable variates not chi/sqrt(nu).
	"""
	
	homepage = "https://github.com/swihart/mvgb"
	cran = "mvgb" 

	version("0.0.4", md5="dd101f34c0b68ee77480df083dae90ee")

	depends_on("r@3.4:", type=("build", "run"))
