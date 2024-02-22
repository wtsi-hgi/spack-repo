# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMns(RPackage):
	"""Mixed Neighbourhood Selection

	An implementation of the mixed neighbourhood selection (MNS) algorithm. The MNS algorithm can be used to estimate multiple related precision matrices. In particular, the motivation behind this work was driven by the need to understand functional connectivity networks across multiple subjects. This package also contains an implementation of a novel algorithm through which to simulate multiple related precision matrices which exhibit properties frequently reported in neuroimaging analysis. 
	"""
	
	cran = "MNS" 

	version("1.0", md5="ed3d0dab99fd977673000d23e7f35214")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
