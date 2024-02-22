# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgeoda(RPackage):
	"""R Library for Spatial Data Analysis

	Provides spatial data analysis functionalities including Exploratory Spatial Data Analysis, 
    Spatial Cluster Detection and Clustering Analysis, Regionalization, etc. based on the C++ source code 
    of 'GeoDa', which is an open-source software tool that serves as an introduction to spatial data analysis.
    The 'GeoDa' software and its documentation are available at <https://geodacenter.github.io>.
	"""
	
	homepage = "https://github.com/geodacenter/rgeoda/"
	cran = "rgeoda" 

	version("0.0.10-4", md5="2b0499e24d7b858e4e10cb71eda8b8e7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
