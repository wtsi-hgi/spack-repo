# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROvlCi(RPackage):
	"""Inference on the Overlap Coefficient: The Binormal Approach and
Alternatives

	Provides functions to construct confidence intervals for the Overlap Coefficient (OVL). OVL measures the similarity between two distributions through the overlapping area of their distribution functions. Given its intuitive description and ease of visual representation by the straightforward depiction of the amount of overlap between the two corresponding histograms based on samples of measurements from each one of the two distributions, the development of accurate methods for confidence interval construction can be useful for applied researchers. Implements methods based on the work of Franco-Pereira, A.M., Nakas, C.T., Reiser, B., and Pardo, M.C. (2021) <doi:10.1177/09622802211046386>.
	"""
	
	cran = "OVL.CI" 

	version("0.1.0", md5="29a6aa88133019411b0ff12b9df5b6af")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
