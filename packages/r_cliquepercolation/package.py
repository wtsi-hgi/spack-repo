# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCliquepercolation(RPackage):
	"""Clique Percolation for Networks

	Clique percolation community detection for weighted and
    unweighted networks as well as threshold and plotting functions.
    For more information see Farkas et al. (2007) <doi:10.1088/1367-2630/9/6/180>
    and Palla et al. (2005) <doi:10.1038/nature03607>.
	"""
	
	cran = "CliquePercolation" 

	version("0.4.0", md5="c5cd3f4dfe41bafe2ed8ea2989761936")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-polychrome", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-lessr", type=("build", "run"))
	depends_on("r-ohenery", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
