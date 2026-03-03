# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaveletmlbestfl(RPackage):
	"""The Best Wavelet Filter-Level for Prepared Wavelet-Based Models

	Four filters have been chosen namely 'haar', 'c6', 'la8', and 'bl14' (Kindly refer to 'wavelets' in 'CRAN' repository for more supported filters). Levels of decomposition are 2, 3, 4, etc. up to maximum decomposition level which is ceiling value of logarithm of length of the series base 2. For each combination two models are run separately. Results are stored in 'input'. First five metrics are expected to be minimum and last three metrics are expected to be maximum for a model to be considered good. Firstly, every metric value (among first five) is searched in every columns and minimum values are denoted as 'MIN' and other values are denoted as 'NA'. Secondly, every metric (among last three) is searched in every columns and maximum values are denoted as 'MAX' and other values are denoted as 'NA'. 'output' contains the similar number of rows (which is 8) and columns (which is number filter-level combinations) as of 'input'. Values in 'output' are corresponding 'NA', 'MIN' or 'MAX'. Finally, the column containing minimum number of 'NA' values is denoted as the best ('FL'). In special case, if two columns having equal 'NA', it has been checked among these two columns which one is having least 'NA' in first five rows and has been inferred as the best. 'FL_metrics_values' are the corresponding metrics values. 'WARIGAANbest' is the data frame (dimension: 1*8) containing different metrics of the best filter-level combination.  More details can be found in Garai and others (2023) <doi:10.13140/RG.2.2.11977.42087>.
	"""
	
	cran = "WaveletMLbestFL" 

	version("0.1.0", md5="a860622418f78b53e01cd016ca19f77f")

	depends_on("r-waveletml", type=("build", "run"))
	depends_on("r-ceemdanml", type=("build", "run"))
	depends_on("r-describedf", type=("build", "run"))
