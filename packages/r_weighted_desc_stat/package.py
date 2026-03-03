# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeightedDescStat(RPackage):
	"""Weighted Descriptive Statistics

	Weighted descriptive statistics is the discipline of quantitatively describing the main features of real-valued fuzzy data which usually given from a fuzzy population. One can summarize this special kind of fuzzy data numerically or graphically using this package. To interpret some of the properties of one or several sets of real-valued fuzzy data, numerically summarize is possible by some weighted statistics which are designed in this package such as mean, variance, covariance and correlation coefficent. Also, graphically interpretation can be given by weighted histogram and weighted scatter plot using this package to describe properties of real-valued fuzzy data set.
	"""
	
	cran = "Weighted.Desc.Stat" 

	version("1.0", md5="2c4b3bbaca172e1e454e857920bcb82e")

