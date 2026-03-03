# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubtite(RPackage):
	"""Subgroup Specific Optimal Dose Assignment

	Chooses subgroup specific optimal doses in a phase I dose finding clinical trial allowing for subgroup combination and simulates clinical trials under the subgroup specific time to event continual reassessment method.  Chapple, A.G., Thall, P.F. (2018) <doi:10.1002/pst.1891>.
	"""
	
	cran = "SubTite" 

	version("4.0.5", md5="8dbd0e24d6aa9ebfcf4b860640bd0a24")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
