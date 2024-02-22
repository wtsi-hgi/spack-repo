# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlgraphics(RPackage):
	"""User Oriented Plotting Functions

	Plots with high flexibility and easy handling, including
  informative regression diagnostics for many models.
	"""
	
	cran = "plgraphics" 

	version("1.2", md5="55723cbeadddc09f7de47f271cd0bdd3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
