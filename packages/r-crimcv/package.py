# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrimcv(RPackage):
	"""Group-Based Modelling of Longitudinal Data

	A finite mixture of Zero-Inflated Poisson (ZIP) models for analyzing criminal trajectories.
	"""
	
	cran = "crimCV" 

	version("1.0.0", md5="4ab27133451b6900f0afc5f8a37cc088")

	depends_on("r@3.5:", type=("build", "run"))
