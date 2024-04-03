# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrandep(RPackage):
	"""Network Analysis of Dependencies of CRAN Packages

	The dependencies of CRAN packages can be analysed in a network fashion. For each package we can obtain the packages that it depends, imports, suggests, etc. By iterating this procedure over a number of packages, we can build, visualise, and analyse the dependency network, enabling us to have a bird's-eye view of the CRAN ecosystem. One aspect of interest is the number of reverse dependencies of the packages, or equivalently the in-degree distribution of the dependency network. This can be fitted by the power law and/or an extreme value mixture distribution <arXiv:2008.03073>, of which functions are provided.
	"""
	
	homepage = "https://github.com/clement-lee/crandep"
	cran = "crandep" 

	version("0.3.6", md5="38999dff4fc872b9f7a0c7a10f755b1c")
	version("0.3.7", md5="54275879dc48016d3ff4af431ce4eae0")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
