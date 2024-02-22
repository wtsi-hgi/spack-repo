# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutothresholdr(RPackage):
	"""An R Port of the 'ImageJ' Plugin 'Auto Threshold'

	Algorithms for automatically finding appropriate thresholds
    for numerical data, with special functions for thresholding images.
    Provides the 'ImageJ' 'Auto Threshold' plugin functionality to R
    users. See <https://imagej.net/plugins/auto-threshold> and Landini et
    al.  (2017) <DOI:10.1111/jmi.12474>.
	"""
	
	homepage = "https://rorynolan.github.io/autothresholdr/"
	cran = "autothresholdr" 

	version("1.4.2", md5="4dc02b67f7d0e732d07d160a941894f6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate@1.9.3:", type=("build", "run"))
	depends_on("r-ijtiff@2.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp@1.0.11:", type=("build", "run"))
	depends_on("r-rlang@0.3.3:", type=("build", "run"))
	depends_on("r-strex@1.4.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
