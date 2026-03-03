# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmass2(RPackage):
	"""Repeated Measures with Attrition: Sample Sizes and Power Levels
for 2 Groups

	For the calculation of sample size or power in a two-group repeated measures design, accounting for attrition and accommodating a variety of correlation structures for the repeated measures; details of the method can be found in the scientific paper: Donald Hedeker, Robert D. Gibbons, Christine Waternaux (1999) <doi:10.3102/10769986024001070>.
	"""
	
	cran = "rmass2" 

	version("0.0.0.2", md5="39a8baa0c6c6f2f2f154243e43bd7044", url="https://cran.r-project.org/src/contrib/rmass2_0.0.0.2.tar.gz")

