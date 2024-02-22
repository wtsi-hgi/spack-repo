# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRem(RPackage):
	"""Relational Event Models (REM)

	Calculate endogenous network effects in event sequences and fit relational event models (REM): Using network event sequences (where each tie between a sender and a target in a network is time-stamped), REMs can measure how networks form and evolve over time. Endogenous patterns such as popularity effects, inertia, similarities, cycles or triads can be calculated and analyzed over time.
	"""
	
	cran = "rem" 

	version("1.3.1", md5="6527f77a84b26d4b77693e1231a3a15e")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
