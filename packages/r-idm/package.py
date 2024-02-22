# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdm(RPackage):
	"""Incremental Decomposition Methods

	Incremental Multiple Correspondence Analysis and Principal
    Component Analysis.
	"""
	
	cran = "idm" 

	version("1.8.3", md5="8a726ab2037f18aef828a4689c963bbf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-animation", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-ca", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("imagemagick", type=("build", "link", "run"))
