# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsmseda(RPackage):
	"""Exploratory Data Analysis of LC-MS/MS data by spectral counts

	Exploratory data analysis to assess the quality of a set of LC-MS/MS experiments, and visualize de influence of the involved factors.
	"""
	
	bioc = "msmsEDA"

	version("1.46.0", commit="f2d10a2ad7fec19d56561401b4aa030ed75d1eda")
	version("1.40.0", commit="4137b239a1003d6e4b7ff0904c54defc85b190a5")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-msnbase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
