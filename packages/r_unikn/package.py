# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnikn(RPackage):
	"""Graphical Elements of the University of Konstanz's Corporate
Design

	Define and use graphical elements of corporate design manuals in R. The 'unikn' package provides color functions (by defining dedicated colors and color palettes, and commands for finding, changing, viewing, and using them) and styled text elements (e.g., for marking, underlining, or plotting colored titles). The pre-defined range of colors and text decoration functions is based on the corporate design of the University of Konstanz <https://www.uni-konstanz.de/>, but can be adapted and extended for other purposes or institutions. 
	"""
	
	homepage = "https://CRAN.R-project.org/package=unikn"
	cran = "unikn" 

	version("0.9.0", md5="c78883497308ae5bf7fc2faeb423d623")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
