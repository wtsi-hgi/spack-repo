# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpmsm(RPackage):
	"""Estimation of Transition Probabilities in Multistate Models

	Estimation of transition probabilities for the
	illness-death model and or the three-state progressive model.
	"""
	
	homepage = "https://github.com/arturstat/TPmsm"
	cran = "TPmsm" 

	version("1.2.12", md5="4708ffc62662f20bf391bfaed9e5c3fe")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
