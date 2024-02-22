# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScepterbinary(RPackage):
	"""Stellar CharactEristics Pisa Estimation gRid for Binary Systems

	SCEPtER pipeline for estimating the stellar age for double-lined detached binary systems. The observational constraints adopted in the recovery are the effective temperature, the metallicity [Fe/H], the mass, and the radius of the two stars. The results are obtained adopting a maximum likelihood technique over a grid of pre-computed stellar models.
	"""
	
	cran = "SCEPtERbinary" 

	version("0.1-1", md5="6ed0b50b0a656e111717b004db56f4ce")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-scepter", type=("build", "run"))
