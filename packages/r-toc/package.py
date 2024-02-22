# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToc(RPackage):
	"""Total Operating Characteristic Curve and ROC Curve

	Construction of the Total Operating Characteristic (TOC) Curve and the Receiver (aka Relative) Operating Characteristic (ROC) Curve for spatial and non-spatial data. The TOC method is a modification of the ROC method which measures the ability of an index variable to diagnose either presence or absence of a characteristic. The diagnosis depends on whether the value of an index variable is above a threshold. Each threshold generates a two-by-two contingency table, which contains four entries: hits (H), misses (M), false alarms (FA), and correct rejections (CR). While ROC shows for each threshold only two ratios, H/(H + M) and FA/(FA + CR), TOC reveals the size of every entry in the contingency table for each threshold (Pontius Jr., R.G., Si, K. 2014. <doi:10.1080/13658816.2013.862623>). 
	"""
	
	homepage = "https://github.com/amsantac/TOC"
	cran = "TOC" 

	version("0.0-6", md5="827e9af25552cfc4919ab58bb9937e11")

	depends_on("r-terra", type=("build", "run"))
	depends_on("r-bit", type=("build", "run"))
