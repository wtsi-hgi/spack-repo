# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsrn(RPackage):
	"""Scan Statistics for Railway Network

	Implement the algorithm provided in scan for estimating the 
  transmission route on railway network using passenger volume. It is a 
  generalization of the scan statistic approach for railway network to identify
  the hot railway route for transmitting infectious diseases. 
	"""
	
	homepage = "https://github.com/uribo/ssrn"
	cran = "ssrn" 

	version("0.1.0", md5="13b8e19a9cbfca4f0393219b4ed83728")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
