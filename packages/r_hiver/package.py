# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHiver(RPackage):
	"""2D and 3D Hive Plots for R

	Creates and plots 2D and 3D hive plots. Hive plots are a unique method of displaying networks of many types in which node properties are mapped to axes using meaningful properties rather than being arbitrarily positioned.  The hive plot concept was invented by Martin Krzywinski at the Genome Science Center (www.hiveplot.net/).  Keywords: networks, food webs, linnet, systems biology, bioinformatics.
	"""
	
	homepage = "https://github.com/bryanhanson/HiveR"
	cran = "HiveR" 

	version("0.3.63", md5="17dbe21515cc193b863653dcf6b3def8")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
