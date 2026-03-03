# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLarf(RPackage):
	"""Local Average Response Functions for Instrumental Variable
Estimation of Treatment Effects

	Provides instrumental variable estimation of treatment effects when both the endogenous treatment and its instrument are binary. Applicable to both binary and continuous outcomes.
	"""
	
	cran = "LARF" 

	version("1.4", md5="25ebf07e8aff64e4fdaae0fa78ba4eba")

	depends_on("r-formula", type=("build", "run"))
