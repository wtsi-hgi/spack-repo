# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBullwhipgame(RPackage):
	"""Bullwhip Effect Demo in Shiny

	The bullwhipgame is an educational game that has as purpose the illustration and exploration of the bullwhip effect,i.e, the increase in demand variability along the supply chain. Marchena Marlene (2010) <arXiv:1009.3977>.  
	"""
	
	cran = "bullwhipgame" 

	version("0.1.0", md5="d31261e1ad4f76288604857dd355f1d3")

	depends_on("r-shiny", type=("build", "run"))
