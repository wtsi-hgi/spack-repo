# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInteractiontest(RPackage):
	"""Calculates Critical Test Statistics to Control False Discovery
Rates in Marginal Effects Plots

	Implements the procedures suggested in Esarey and Sumner (2017) <http://justinesarey.com/interaction-overconfidence.pdf> for controlling the false discovery rate when constructing marginal effects plots for models with interaction terms.
	"""
	
	cran = "interactionTest" 

	version("1.2", md5="c73c29c64cc1d2b9c159682621958dbe")

	depends_on("r@3.4:", type=("build", "run"))
