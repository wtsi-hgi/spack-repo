# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMercator(RPackage):
	"""Clustering and Visualizing Distance Matrices

	Defines the classes used to explore, cluster and
  visualize distance matrices, especially those arising from binary
  data. See Abrams and colleagues, 2021, <doi:10.1093/bioinformatics/btab037>.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "Mercator" 

	version("1.1.2", md5="2422b8e48e6ca5764c497cc2d9b96df9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-thresher@1.1:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-classdiscovery", type=("build", "run"))
	depends_on("r-polychrome", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-kohonen", type=("build", "run"))
