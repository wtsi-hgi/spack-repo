# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdrsamplesize2(RPackage):
	"""Computing Power and Sample Size for the False Discovery Rate in
Multiple Applications

	Defines a collection of functions to compute average power and sample size for studies that use the false discovery rate as the final measure of statistical significance. A three-rectangle approximation method of a p-value histogram is proposed to derive a formula to compute the statistical power for analyses that involve the FDR. The methodology paper of this package is under review.
	"""
	
	cran = "FDRsamplesize2" 

	version("0.2.0", md5="93e5a2137e29ad8d93b9ef2f78833e93", url="https://cran.r-project.org/src/contrib/FDRsamplesize2_0.2.0.tar.gz")
	version("0.1.0", md5="ef96c1b5f2895a321c29b8cd358ae3dc", url="https://cran.r-project.org/src/contrib/FDRsamplesize2_0.1.0.tar.gz")

