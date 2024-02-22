# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RL2e(RPackage):
	"""Robust Structured Regression via the L2 Criterion

	An implementation of a computational framework for performing robust structured regression with the L2 criterion 
             from Chi and Chi (2021+). Improvements using the majorization-minimization (MM) principle from Liu, Chi, and 
             Lange (2022+) added in Version 2.0.
	"""
	
	cran = "L2E" 

	version("2.0", md5="ce64ae2e0df97a122eba51fe21c522c1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-osqp", type=("build", "run"))
	depends_on("r-isotone", type=("build", "run"))
	depends_on("r-cobs", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
