# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmdiallel(RPackage):
	"""Linear Fixed/Mixed Effects Models for Diallel Crosses

	Several service functions to be used to analyse datasets obtained from diallel experiments within the frame of linear models in R, as described in  Onofri et al (2020) <DOI:10.1007/s00122-020-03716-8>.
	"""
	
	homepage = "https://www.statforbiology.com/lmDiallel/"
	cran = "lmDiallel" 

	version("1.0.1", md5="19cee0f1fcf07211c8808d5307e4cfcb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-sommer", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
