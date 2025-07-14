# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMade4(RPackage):
	"""Multivariate analysis of microarray data using ADE4

	Multivariate data analysis and graphical display of microarray data. Functions include for supervised dimension reduction (between group analysis) and joint dimension reduction of 2 datasets (coinertia analysis). It contains functions that require R package ade4.
	"""
	
	homepage = "http://www.hsph.harvard.edu/aedin-culhane/"
	bioc = "made4"

	version("1.82.0", commit="af8e708e74dff93eee6e67c9c2d73e7941be783f")
	version("1.76.0", commit="4fa62322cf560d2720055f48c1dcf46f5bc5d745")

	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
