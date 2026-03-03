# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemblance(RPackage):
	"""A Data-Driven Similarity Kernel on Probability Spaces

	We present a rank-based Mercer kernel to compute a pair-wise similarity metric corresponding to informative representation of data. We tailor the development of a kernel to encode our prior knowledge about the data distribution over a probability space. The philosophical concept behind our construction is that objects whose feature values fall on the extreme of that feature’s probability mass distribution are more similar to each other, than objects whose feature values lie closer to the mean. Semblance emphasizes features whose values lie far away from the mean of their probability distribution. The kernel relies on properties empirically determined from the data and does not assume an underlying distribution. The use of feature ranks on a probability space ensures that Semblance is computational efficacious, robust to outliers, and statistically stable, thus making it widely applicable algorithm for pattern analysis. The output from the kernel is a square, symmetric matrix that gives proximity values between pairs of observations.
	"""
	
	cran = "Semblance" 

	version("1.1.0", md5="c8b7b01b072cb23f31c83c34012eb335")

	depends_on("r-fields@9.6:", type=("build", "run"))
	depends_on("r-performanceanalytics@1.5.2:", type=("build", "run"))
	depends_on("r-desctools@0.99.26:", type=("build", "run"))
	depends_on("r-msos@1.1:", type=("build", "run"))
