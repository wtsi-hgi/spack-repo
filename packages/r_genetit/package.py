# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenetit(RPackage):
	"""Spatial Graph-Theoretic Genetic Gravity Modelling

	Implementation of spatial graph-theoretic genetic gravity models.
    The model framework is applicable for other types of spatial flow questions.
    Includes functions for constructing spatial graphs, sampling and summarizing
    associated raster variables and building unconstrained and singly constrained
    gravity models.
	"""
	
	homepage = "https://github.com/jeffreyevans/GeNetIt"
	cran = "GeNetIt" 

	version("0.1-6", md5="9d45bef5e89331afde41727dd6c80853")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-exactextractr", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sfnetworks", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
