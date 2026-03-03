# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMra(RPackage):
	"""Mark-Recapture Analysis

	Accomplishes mark-recapture analysis with covariates. Models available include the Cormack-Jolly-Seber open population (Cormack (1972) <doi:10.2307/2556151>; Jolly (1965) <doi:10.2307/2333826>; Seber (1965) <doi:10.2307/2333827>) and Huggin's (1989) <doi:10.2307/2336377> closed population. 
	Link functions include logit, sine, and hazard.  Model selection, model averaging, plot, and simulation routines included. Open population size by the Horvitz-Thompson (1959) <doi:10.2307/2280784> estimator.
	"""
	
	cran = "mra" 

	version("2.16.11", md5="0462486dc4efc549609338b2085a3350")

