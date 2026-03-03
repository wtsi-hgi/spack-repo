# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataviz(RPackage):
	"""Data Visualisation Using an HTML Page and 'D3.js'

	Gives access to data visualisation methods that are relevant from the statistician's point of view. Using 'D3''s existing data visualisation tools to empower R language and environment. The throw chart method is a line chart used to illustrate paired data sets (such as before-after, male-female).
	"""
	
	cran = "DataViz" 

	version("0.2.8", md5="bc482dd0da5e15da1fded0d0f4ff3c53")

	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
