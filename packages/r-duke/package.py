# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDuke(RPackage):
	"""Creating a Color-Blind Friendly Duke Color Package

	Generates visualizations with Duke’s official suite of colors in a color blind friendly way.
	"""
	
	homepage = "https://github.com/aidangildea/duke"
	cran = "duke" 

	version("0.0.3", md5="6c29b2152e56ad9a2371b0e3c9fbb8be")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
