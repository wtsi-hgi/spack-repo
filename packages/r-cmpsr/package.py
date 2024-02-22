# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmpsr(RPackage):
	"""R Implementation of Congruent Matching Profile Segments Method

	This is an open-source implementation of the Congruent Matching Profile 
    Segments (CMPS) method (Chen et al. 2019)<doi:10.1016/j.forsciint.2019.109964>. 
    In general, it can be used for objective comparison of striated tool marks, and in our 
    examples, we specifically use it for bullet signatures comparisons. The CMPS score is 
    expected to be large if two signatures are similar. So it can also be considered as a 
    feature that measures the similarity of two bullet signatures.
	"""
	
	cran = "cmpsR" 

	version("0.1.2", md5="d40f94602aed3d73172bd56984e27a49")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.5:", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
