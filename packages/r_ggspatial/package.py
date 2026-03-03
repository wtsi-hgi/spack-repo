# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgspatial(RPackage):
	"""Spatial Data Framework for ggplot2

	Spatial data plus the power of the ggplot2 framework means easier mapping when input 
  data are already in the form of spatial objects.
	"""
	
	homepage = "https://paleolimbot.github.io/ggspatial/"
	cran = "ggspatial" 

	version("1.1.9", md5="fe4d3a48027bd84c80d422b7479f9e69")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-rosm@0.2:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
