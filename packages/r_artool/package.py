# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArtool(RPackage):
	"""Aligned Rank Transform

	The aligned rank transform for nonparametric
    factorial ANOVAs as described by Wobbrock,
    Findlater, Gergle, and Higgins (2011) <doi:10.1145/1978942.1978963>. 
    Also supports aligned rank transform contrasts as described
    by Elkin, Kay, Higgins, and Wobbrock (2021)
    <doi:10.1145/3472749.3474784>.
	"""
	
	homepage = "https://github.com/mjskay/ARTool/"
	cran = "ARTool" 

	version("0.11.1", md5="33ac3a2b000284905cd8c79953345762")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-car@2.0.24:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
