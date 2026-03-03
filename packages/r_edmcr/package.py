# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdmcr(RPackage):
	"""Euclidean Distance Matrix Completion Tools

	Implements various general algorithms to estimate missing elements
   of a Euclidean (squared) distance matrix.  
   Includes optimization methods based on semi-definite programming found in
   Alfakih, Khadani, and Wolkowicz (1999)<doi:10.1023/A:1008655427845>, 
   a non-convex position formulation by Fang and O'Leary (2012)<doi:10.1080/10556788.2011.643888>, and 
   a dissimilarity parameterization formulation by Trosset (2000)<doi:10.1023/A:1008722907820>.
   When the only non-missing
   distances are those on the minimal spanning tree, the guided random search
   algorithm will complete the matrix while preserving the minimal spanning tree following
   Rahman and Oldford (2018)<doi:10.1137/16M1092350>.
   Point configurations in specified dimensions can be determined from the completions. 
   Special problems such as the sensor localization problem, 
   as for example in Krislock and Wolkowicz (2010)<doi:10.1137/090759392>,
   as well as reconstructing
   the geometry of a molecular structure, as for example in 
   Hendrickson (1995)<doi:10.1137/0805040>, can also be solved.
   These and other methods are described in the thesis of Adam Rahman(2018)<https://hdl.handle.net/10012/13365>.
	"""
	
	homepage = "https://github.com/great-northern-diver/edmcr"
	cran = "edmcr" 

	version("0.2.0", md5="f197fcc09efe0b9e7a9b244c0c190a60")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lbfgs", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-sdpt3r", type=("build", "run"))
