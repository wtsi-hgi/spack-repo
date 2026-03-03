# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScepter(RPackage):
	"""Stellar CharactEristics Pisa Estimation gRid

	A pipeline for estimating the stellar
        age, mass, and radius given observational 
        effective temperature, [Fe/H], and astroseismic
	parameters. The results are obtained adopting a maximum likelihood
	technique over a grid of pre-computed stellar models, as
	described in Valle et al. (2014) <doi:10.1051/0004-6361/201322210>.
	"""
	
	cran = "SCEPtER" 

	version("0.2-4", md5="93210afc7d58c0f925ecb4f0a56909f4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
