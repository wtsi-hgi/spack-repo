# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerutimber(RPackage):
	"""Catalogue of the Timber Forest Species of the Peruvian Amazon

	Access the data of the 'Catalogue of the Timber Forest Species of the Peruvian Amazon' Vásquez Martínez, R., & Rojas Gonzáles, R.D.P.(2022)<doi:10.21704/rfp.v37i3.1956>.
	"""
	
	homepage = "https://github.com/PaulESantos/perutimber"
	cran = "perutimber" 

	version("0.1.0", md5="42368bed271e3fb2f30f2546b680dd50")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
