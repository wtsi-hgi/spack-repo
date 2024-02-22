# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiaplt(RPackage):
	"""Beads Summary Plot of Ranges

	Visualize one-factor data frame. 
  Beads plot consists of diamonds of each factor of each data series. 
  A diamond indicates average and range. 
  Look over a data frame with many numeric columns and a factor column. 
	"""
	
	cran = "diaplt" 

	version("1.4.0", md5="4a6d10fcae63ab134616933156637949")

