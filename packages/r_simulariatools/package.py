# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimulariatools(RPackage):
	"""Simularia Tools for the Analysis of Air Pollution Data

	A set of tools developed at Simularia for Simularia, to help
    preprocessing and post-processing of meteorological and air quality data.
	"""
	
	homepage = "https://www.simularia.it/simulariatools/"
	cran = "simulariatools" 

	version("2.5.1", md5="4cc63147a07be2decd31ead43c3018f4")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
