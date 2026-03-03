# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigmatch(RPackage):
	"""Making Optimal Matching Size-Scalable Using Optimal Calipers

	Implements optimal matching with near-fine balance in large observational studies with the use of optimal calipers to get a sparse network. The caliper is optimal in the sense that it is as small as possible such that a matching exists. The main functions in the 'bigmatch' package are optcal() to find the optimal caliper, optconstant() to find the optimal number of nearest neighbors, and nfmatch() to find a near-fine balance match with a caliper and a restriction on the number of nearest neighbors. 
    Yu, R., Silber, J. H., and Rosenbaum, P. R. (2020). <DOI:10.1214/19-sts699>. 
	"""
	
	cran = "bigmatch" 

	version("0.6.4", md5="97d768fdaa87d69e8f7ab73c94b44832")

	depends_on("r-rcbalance", type=("build", "run"))
	depends_on("r-liqueuer", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
