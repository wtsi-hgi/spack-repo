# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvomorph(RPackage):
	"""Evolutionary Morphometric Simulation

	Evolutionary process simulation using geometric morphometric data. Manipulation of landmark data files (TPS), shape plotting and distances plotting functions.
	"""
	
	cran = "Evomorph" 

	version("0.9", md5="6fa7f41b262cb437de293a6cb4d5f3f4")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-geomorph", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
