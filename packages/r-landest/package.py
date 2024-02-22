# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLandest(RPackage):
	"""Landmark Estimation of Survival and Treatment Effect

	Provides functions to estimate survival and a treatment effect using a landmark estimation approach.
	"""
	
	cran = "landest" 

	version("1.2", md5="a6f20bf07a07afa23a5167402834b8d2")

	depends_on("r-survival", type=("build", "run"))
