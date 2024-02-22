# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoon(RPackage):
	"""Interactive Statistical Data Visualization

	An extendable toolkit for interactive data visualization and exploration.
	"""
	
	homepage = "https://great-northern-diver.github.io/loon/"
	cran = "loon" 

	version("1.4.1", md5="a39832b2ac905e6ef46594352adaa77f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
