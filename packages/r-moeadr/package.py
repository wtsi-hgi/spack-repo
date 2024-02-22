# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoeadr(RPackage):
	"""Component-Wise MOEA/D Implementation

	Modular implementation of Multiobjective Evolutionary Algorithms 
              based on Decomposition (MOEA/D) [Zhang and Li (2007), 
              <DOI:10.1109/TEVC.2007.892759>] for quick assembling and 
              testing of new algorithmic components, as well as easy 
              replication of published MOEA/D proposals. The full framework is
              documented in a paper published in the Journal of Statistical 
              Software [<doi:10.18637/jss.v092.i06>].
	"""
	
	homepage = "https://fcampelo.github.io/MOEADr/"
	cran = "MOEADr" 

	version("1.1.3", md5="147a2b5de6570469366ea50b3d438fe7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
