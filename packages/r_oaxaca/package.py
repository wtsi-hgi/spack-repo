# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROaxaca(RPackage):
	"""Blinder-Oaxaca Decomposition

	An implementation of the Blinder-Oaxaca decomposition for linear regression models.
	"""
	
	cran = "oaxaca" 

	version("0.1.5", md5="e83db06e808f1e2835a37aeb13a91455")

	depends_on("r-formula", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
