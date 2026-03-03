# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKuiper2samp(RPackage):
	"""Two-Sample Kuiper Test

	This function performs the two-sample Kuiper test to assess the anomaly of continuous, one-dimensional probability distributions. References used for this method are (1). Kuiper, N. H. (1960). <DOI:10.1016/S1385-7258(60)50006-0> and (2). Paltani, S. (2004). <DOI:10.1051/0004-6361:20034220>. 
	"""
	
	cran = "kuiper.2samp" 

	version("1.0", md5="6daadaeae3ec1bf2d8ea8ff72218ac44")

	depends_on("r@3.3.1:", type=("build", "run"))
