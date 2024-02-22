# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmitidvisu(RPackage):
	"""Visualize Data for Host and Viral Population from 'SMITIDstruct'
using 'HTMLwidgets'

	Visualisation tools for 'SMITIDstruct' package.
  Allow to visualize host timeline, transmission tree, index diversities
  and variant graph using 'HTMLwidgets'. It mainly using 'D3JS' javascript framework.
	"""
	
	homepage = "https://informatique-mia.inrae.fr/biosp/anr-smitid-project/"
	cran = "SMITIDvisu" 

	version("0.0.9", md5="ff67b2603e8ce62bde98dbcf4818971b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-htmlwidgets@0.3.2:", type=("build", "run"))
	depends_on("r-yaml@2.1.16:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
