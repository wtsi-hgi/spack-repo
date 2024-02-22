# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNfwdist(RPackage):
	"""The Standard Distribution Functions for the 3D NFW Profile

	Density, distribution function, quantile function and random generation for the 3D Navarro, Frenk & White (NFW) profile. For details see Robotham & Howlett (2018) <arXiv:1805.09550>.
	"""
	
	cran = "NFWdist" 

	version("0.1.0", md5="3011fdaa95d9d214176deac908e17970")

	depends_on("r@3:", type=("build", "run"))
