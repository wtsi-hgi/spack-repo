# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInca(RPackage):
	"""Integer Calibration

	Specific functions are provided for rounding real weights to integers and performing an integer programming algorithm for calibration problems. They are useful for census-weights adjustments, or for performing linear regression with integer parameters. This research was supported in part by the U.S. Department of Agriculture, National Agriculture Statistics Service. The findings and conclusions in this publication are those of the authors and should not be construed to represent any official USDA, or US Government determination or policy.
	"""
	
	cran = "inca" 

	version("0.0.4", md5="e4a1f8f61ceae8e344f2bb30efefde41")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
