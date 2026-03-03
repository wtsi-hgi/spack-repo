# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKlustr(RPackage):
	"""D3 Dynamic Cluster Visualizations

	Used to create dynamic, interactive 'D3.js' 
  based parallel coordinates and principal component plots in 'R'.
  The plots make visualizing k-means or other clusters simple and informative.
	"""
	
	homepage = "https://mckaymdavis.github.io/klustR/"
	cran = "klustR" 

	version("0.1.0", md5="dc1982581405a40b1c9458a93eb0693c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-htmlwidgets@0.3.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
