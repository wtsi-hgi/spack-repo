# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowchic(RPackage):
	"""Analyze flow cytometric data using histogram information

	A package to analyze flow cytometric data of complex microbial communities based on histogram images
	"""
	
	homepage = "http://www.ufz.de/index.php?en=16773"
	bioc = "flowCHIC"

	version("1.42.0", commit="6fc189bda7981c622dc2b43df8d1f0b92fc430c2")
	version("1.36.0", commit="2a131a453cc60c27af5ddc36fc63b89421dd0b91")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
