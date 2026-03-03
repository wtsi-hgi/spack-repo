# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLorenz(RPackage):
	"""Tools for Deriving Income Inequality Estimates from Grouped
Income Data

	Provides two methods of estimating income inequality statistics from binned income data, such as the income data provided in the Census.
  These methods use different interpolation techniques to infer the distribution of incomes within income bins.  One method is an implementation of 
  Jargowsky and Wheeler's mean-constrained integration over brackets (MCIB).  The other method is based on a new technique, Lorenz interpolation, 
  which estimates income inequality by constructing an interpolated Lorenz curve based on the binned income data.  These methods can be used to 
  estimate three income inequality measures: the Gini (the default measure returned), the Theil, and the Atkinson's index.  
  Jargowsky and Wheeler (2018) <doi:10.1177/0081175018782579>.
	"""
	
	cran = "lorenz" 

	version("0.1.0", md5="36ffa046d756959a30c702f038ab8cbe")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dineq", type=("build", "run"))
