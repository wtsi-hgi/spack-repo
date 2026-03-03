# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhcoclust(RPackage):
	"""Robust Hierarchical Co-Clustering to Identify Significant
Co-Cluster

	Here we performs robust hierarchical co-clustering between row and column entities of a data matrix in 
             absence and presence of outlying observations. It can be used to explore important co-clusters consisting of  
             important samples and their regulatory significant features. Please see Hasan, Badsha and Mollah (2020) 
             <doi:10.1101/2020.05.13.094946>.
	"""
	
	cran = "rhcoclust" 

	version("2.0.0", md5="512282dafe7d5225c2e00691162d087e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
