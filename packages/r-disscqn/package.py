# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisscqn(RPackage):
	"""Multiple Assemblage Dissimilarity for Orders q = 0-N

	Calculate multiple or pairwise dissimilarity for orders q = 0-N 
    (CqN; Chao et al. 2008 <doi:10/fcvn63>) for a set of species assemblages or 
    interaction networks.
	"""
	
	homepage = "https://murphymv.github.io/dissCqN/"
	cran = "dissCqN" 

	version("0.1.0", md5="6e980a0dc936c7c237d33b492dbecb09")

	depends_on("r@4:", type=("build", "run"))
