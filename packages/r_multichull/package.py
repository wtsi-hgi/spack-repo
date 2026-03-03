# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultichull(RPackage):
	"""A Generic Convex-Hull-Based Model Selection Method

	Given a set of models for which a measure of model (mis)fit and model complexity is provided, CHull(), developed by Ceulemans and Kiers (2006) <doi:10.1348/000711005X64817>, determines the models that are located on the boundary of the convex hull and selects an optimal model by means of the scree test values. 
	"""
	
	cran = "multichull" 

	version("1.0.1", md5="f6ef92cb8867b5a005c33ae25f2abe12")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
