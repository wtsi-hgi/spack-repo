# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwgraph(RPackage):
	"""Random Walks on Graphs Representing a Transactional Network

	Random walk functions to extract new variables based on clients transactional behaviour. For more details, see Eddin et al. (2021) <arXiv:2112.07508v3> and Oliveira et al. (2021) <arXiv:2102.05373v2>. 
	"""
	
	cran = "RWgraph" 

	version("1.0.0", md5="067fb0c278d53fb6e2d6ee78710d304f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
