# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDarkdiv(RPackage):
	"""Estimating Dark Diversity and Site-Specific Species Pools

	Estimation of dark diversity and site-specific species pools using species co-occurrences. 
    It includes implementations of probabilistic dark diversity based on the 
    Hypergeometric distribution, as well as estimations based on the Beals index,
    which can be transformed to binary predictions using different thresholds, 
    or transformed into a favorability index. All methods include the possibility of
    using a calibration dataset that is used to estimate the indication matrix 
    between pairs of species, or to estimate dark diversity directly on a single 
    dataset. See De Caceres and Legendre (2008) <doi:10.1007/s00442-008-1017-y>, 
    Lewis et al. (2016) <doi:10.1111/2041-210X.12443>, 
    Partel et al. (2011) <doi:10.1016/j.tree.2010.12.004>, Real et al. (2017) <doi:10.1093/sysbio/syw072>
    for further information.
	"""
	
	cran = "DarkDiv" 

	version("0.3.0", md5="787e0187a5cf7479a3c992a5b9818063")

	depends_on("r-vegan", type=("build", "run"))
