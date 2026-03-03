# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigdatadist(RPackage):
	"""Distances for Machine Learning and Statistics in the Context of
Big Data

	Functions to compute distances between probability measures or any other data object than can be posed in this way, entropy measures for samples of curves, distances and depth measures for functional data, and the Generalized Mahalanobis Kernel distance for high dimensional data. For further details about the metrics please refer to Martos et al (2014) <doi:10.3233/IDA-140706>; Martos et al (2018) <doi:10.3390/e20010033>; Hernandez et al (2018, submitted); Martos et al (2018, submitted).
	"""
	
	cran = "bigdatadist" 

	version("1.1", md5="0db16a1ae806331b7146ed111150e909")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
