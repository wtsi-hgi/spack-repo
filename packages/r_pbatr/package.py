# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbatr(RPackage):
	"""Pedigree/Family-Based Genetic Association Tests Analysis and
Power

	This R package provides power calculations via internal simulation methods. The package also provides a frontend to the now abandoned PBAT program (developed by Christoph Lange), and reads in the corresponding output and displays results and figures when appropriate. The license of this R package itself is GPL. However, to have the program interact with the PBAT program for some functionality of the R package, users must additionally obtain the PBAT program from Christoph Lange, and accept his license. Both the data analysis and power calculations have command line and graphical interfaces using tcltk.
	"""
	
	homepage = "https://academic.oup.com/bioinformatics/article-abstract/22/24/3103/208723"
	cran = "pbatR" 

	version("2.2-17", md5="1756e03b4182092b847a60a7b1a784a5")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
