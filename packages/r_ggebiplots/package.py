# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgebiplots(RPackage):
	"""GGE Biplots with 'ggplot2'

	Genotype plus genotype-by-environment (GGE) biplots rendered using 'ggplot2'. Provides a command line interface to all of the functionality contained within the archived package 'GGEBiplotGUI'.
	"""
	
	cran = "GGEBiplots" 

	version("0.1.3", md5="fa1e79e4481c3cbd61fa93c503463652")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-ggforce@0.1.1:", type=("build", "run"))
	depends_on("r-scales@0.4.1:", type=("build", "run"))
