# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSears(RPackage):
	"""Seamless Dose Escalation/Expansion with Adaptive Randomization
Scheme

	A seamless design that combines phase I dose escalation based on toxicity with phase II dose expansion and dose comparison based on efficacy. 
	"""
	
	cran = "SEARS" 

	version("0.1.0", md5="1a715e6757a67a2f2794342815237d3a")

	depends_on("r-boin", type=("build", "run"))
