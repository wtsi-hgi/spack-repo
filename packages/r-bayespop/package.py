# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayespop(RPackage):
	"""Probabilistic Population Projection

	Generating population projections for all countries of the world using several probabilistic components, such as total fertility rate and life expectancy (Raftery et al., 2012 <doi:10.1073/pnas.1211452109>).
	"""
	
	homepage = "https://bayespop.csss.washington.edu"
	cran = "bayesPop" 

	version("10.0-1", md5="21b542cec5998962a827582786d19aa1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bayestfr@7.1.0:", type=("build", "run"))
	depends_on("r-bayeslife@5.0.0:", type=("build", "run"))
	depends_on("r-mortcast@2.6.1:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-wpp2019", type=("build", "run"))
	depends_on("r-wpp2012", type=("build", "run"))
	depends_on("r-rworldmap", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-googlevis", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
