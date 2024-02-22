# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneraloaxaca(RPackage):
	"""Blinder-Oaxaca Decomposition for Generalized Linear Model

	Perform the Blinder-Oaxaca decomposition for generalized linear 
   model with bootstrapped standard errors. The twofold and threefold 
   decomposition are given, even the generalized linear model output in each group.
	"""
	
	cran = "GeneralOaxaca" 

	version("1.0", md5="db1847506be27fbc0045dd80b22f6383")

	depends_on("r-boot", type=("build", "run"))
