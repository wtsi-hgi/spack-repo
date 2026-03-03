# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwostagete(RPackage):
	"""Two-Stage Threshold Estimation

	Implements a variety of non-parametric methods for computing one-stage and two-stage confidence intervals, as well as point estimates of threshold values.
	"""
	
	cran = "twostageTE" 

	version("1.3", md5="018dfa78412808686259b0d59ceb43ba")

	depends_on("r-isotone", type=("build", "run"))
