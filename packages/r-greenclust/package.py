# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreenclust(RPackage):
	"""Combine Categories Using Greenacre's Method

	Implements a method of iteratively collapsing the rows of a
    contingency table, two at a time, by selecting the pair of categories whose
    combination yields a new table with the smallest loss of chi-squared, as
    described by Greenacre, M.J. (1988) <doi:10.1007/BF01901670>. The result is
    compatible with the class of object returned by the 'stats' package's
    hclust() function and can be used similarly (plotted as a dendrogram,
    cut, etc.). Additional functions are provided for automatic cutting and
    diagnostic plotting.
	"""
	
	homepage = "https://github.com/JeffJetton/greenclust"
	cran = "greenclust" 

	version("1.1.1", md5="0807869923305818d5ca1d924270aed1")

