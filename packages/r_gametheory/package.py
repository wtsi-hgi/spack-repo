# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGametheory(RPackage):
	"""Cooperative Game Theory

	Implementation of a common set of punctual solutions  for Cooperative Game Theory.
	"""
	
	cran = "GameTheory" 

	version("2.7.1", md5="742f27cdfebfd5b356ee6feb6ce5d109")

	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
	depends_on("r-kappalab", type=("build", "run"))
