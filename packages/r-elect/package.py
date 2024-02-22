# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElect(RPackage):
	"""Estimation of Life Expectancies Using Multi-State Models

	Functions to compute state-specific and marginal life expectancies. The computation is based on a fitted continuous-time multi-state model that includes an absorbing death state; see Van den Hout (2017, ISBN:9781466568402). The fitted multi-state model model should be estimated using the 'msm' package using age as the time-scale.
	"""
	
	cran = "elect" 

	version("1.2", md5="505ec98e90c1372b2a555e25e5d0a6e6")

	depends_on("r-msm", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
