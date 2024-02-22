# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdakit(RPackage):
	"""Toolkit for Topological Data Analysis

	Topological data analysis studies structure and shape of the data using topological features. We provide a variety of algorithms to learn with persistent homology of the data based on functional summaries for clustering, hypothesis testing, visualization, and others. We refer to Wasserman (2018) <doi:10.1146/annurev-statistics-031017-100045> for a statistical perspective on the topic. 
	"""
	
	cran = "TDAkit" 

	version("0.1.2", md5="073ae78cdad7c34e1d8fdd8bfb8e3c33")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-tdastats", type=("build", "run"))
	depends_on("r-t4cluster", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-maotai", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
