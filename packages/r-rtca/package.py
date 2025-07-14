# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtca(RPackage):
	"""Open-source toolkit to analyse data from xCELLigence System (RTCA)

	Import, analyze and visualize data from Roche(R) xCELLigence RTCA systems. The package imports real-time cell electrical impedance data into R. As an alternative to commercial software shipped along the system, the Bioconductor package RTCA provides several unique transformation (normalization) strategies and various visualization tools.
	"""
	
	homepage = "http://code.google.com/p/xcelligence/"
	bioc = "RTCA"

	version("1.60.0", commit="915ae56eba0622f2744c10cd6fdcaf0b70e45de0")
	version("1.54.0", commit="50f168ecd3652ab5f415e8bb243ced777aaa75bd")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
