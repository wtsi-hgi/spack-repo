# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAleplot(RPackage):
	"""Accumulated Local Effects (ALE) Plots and Partial Dependence
(PD) Plots

	Visualizes the main effects of individual predictor variables and their second-order interaction effects in black-box supervised learning models. The package creates either Accumulated Local Effects (ALE) plots and/or Partial Dependence (PD) plots, given a fitted supervised learning model.
	"""
	
	cran = "ALEPlot" 

	version("1.1", md5="60c64fbd26cd306fda755fb9a4ec81eb")

	depends_on("r-yaimpute", type=("build", "run"))
