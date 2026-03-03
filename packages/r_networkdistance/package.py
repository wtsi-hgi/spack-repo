# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworkdistance(RPackage):
	"""Distance Measures for Networks

	Network is a prevalent form of data structure in many fields. As an object of analysis, many distance or metric measures have been proposed to define the concept of similarity between two networks. We provide a number of distance measures for networks. See Jurman et al (2011) <doi:10.3233/978-1-60750-692-8-227> for an overview on spectral class of inter-graph distance measures.
	"""
	
	cran = "NetworkDistance" 

	version("0.3.4", md5="42a270f56a9de2898e1168d1d3c57aaa")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-graphon", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
