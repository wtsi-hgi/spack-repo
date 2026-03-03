# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNimbleecology(RPackage):
	"""Distributions for Ecological Models in 'nimble'

	Common ecological distributions for 'nimble' models in the form of nimbleFunction objects. 
  Includes Cormack-Jolly-Seber, occupancy, dynamic occupancy, hidden Markov, dynamic hidden Markov, and N-mixture models.
  (Jolly (1965) <DOI: 10.2307/2333826>, Seber (1965) <DOI: 10.2307/2333827>, Turek et al. (2016) <doi:10.1007/s10651-016-0353-z>).
	"""
	
	homepage = "https://github.com/nimble-dev/nimbleEcology"
	cran = "nimbleEcology" 

	version("0.4.1", md5="f6608ade69be8e0fe10e19e0d54ee90d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-nimble", type=("build", "run"))
