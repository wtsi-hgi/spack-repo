# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNodiv(RPackage):
	"""Compares the Distribution of Sister Clades Through a Phylogeny

	An implementation of the nodiv algorithm, see Borregaard, M.K., Rahbek, C., Fjeldsaa, J., Parra, J.L., Whittaker, R.J. & Graham, C.H. 2014. Node-based analysis of species distributions. Methods in Ecology and Evolution 5(11): 1225-1235. <DOI:10.1111/2041-210X.12283>. Package for phylogenetic analysis of species distributions. The main function goes through each node in the phylogeny, compares the distributions of the two descendant nodes, and compares the result to a null model. This highlights nodes where major distributional divergence have occurred. The distributional divergence for these nodes is mapped.
	"""
	
	homepage = "https://github.com/mkborregaard/nodiv"
	cran = "nodiv" 

	version("1.4.2", md5="d61fa60d790fe5c0205ba30f7447bfc3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-picante", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
