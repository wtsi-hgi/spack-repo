# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQccrs(RPackage):
	"""Quality Control Charts under Repetitive Sampling

	Functions to calculate Average Sample Numbers (ASN), Average Run Length (ARL1) and value of k, k1 and k2 for quality control charts under repetitive sampling as given in Aslam et al. (2014) (<DOI:10.7232/iems.2014.13.1.101>).
	"""
	
	homepage = "https://github.com/myaseen208/qccrs"
	cran = "qccrs" 

	version("0.1.0", md5="4155ea8cb2446a33763363730991e23a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
