# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPim(RPackage):
	"""Fit Probabilistic Index Models

	Fit a probabilistic index model as described in 
    Thas et al, 2012: <doi:10.1111/j.1467-9868.2011.01020.x>. The interface to the 
    modeling function has changed in this new version. The old version is
    still available at R-Forge.
	"""
	
	homepage = "https://github.com/CenterForStatistics-UGent/pim"
	cran = "pim" 

	version("2.0.2", md5="a160d9a2cd958608c8b837eed793eae5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
