# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcca(RPackage):
	"""A Canonical Correlation Analysis with Inferential Guaranties

	It performs Canonical Correlation Analysis and provides inferential guaranties on the correlation components. The p-values are computed following the resampling method developed in Winkler, A. M., Renaud, O., Smith, S. M., & Nichols, T. E. (2020). Permutation inference for canonical correlation analysis. NeuroImage, <doi:10.1016/j.neuroimage.2020.117065>. Furthermore, it provides plotting tools to visualize the results.
	"""
	
	cran = "acca" 

	version("0.2", md5="857facb598cf77e83cc31b3265e18416")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
