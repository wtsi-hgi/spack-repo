# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTempted(RPackage):
	"""Temporal Tensor Decomposition, a Dimensionality Reduction Tool
for Longitudinal Multivariate Data

	
    TEMPoral TEnsor Decomposition (TEMPTED), is a dimension reduction method for multivariate longitudinal data with varying temporal sampling. It formats the data into a temporal tensor and decomposes it into a summation of low-dimensional components, each consisting of a subject loading vector, a feature loading vector, and a continuous temporal loading function. These loadings provide a low-dimensional representation of subjects or samples and can be used to identify features associated with clusters of subjects or samples. TEMPTED provides the flexibility of allowing subjects to have different temporal sampling, so time points do not need to be binned, and missing time points do not need to be imputed.
	"""
	
	homepage = "https://github.com/pixushi/tempted"
	cran = "tempted" 

	version("0.1.0", md5="4636e6eb21a41add784995d89983c271")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-np@0.60.17:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
