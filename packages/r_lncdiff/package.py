# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLncdiff(RPackage):
	"""Long Non-Coding RNA Differential Expression Analysis

	We developed an approach to detect differential expression features in long non-coding RNA low counts, using generalized linear model with zero-inflated exponential quasi likelihood ratio test. Methods implemented in this package are described in Li (2019) <doi:10.1186/s12864-019-5926-4>. 
	"""
	
	cran = "lncDIFF" 

	version("1.0.0", md5="6558a16939667c6e516ca9d38ff61c78")

	depends_on("r@3.5:", type=("build", "run"))
