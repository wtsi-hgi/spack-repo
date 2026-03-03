# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustx(RPackage):
	"""'eXtra' / 'eXperimental' Functionality for Robust Statistics

	Robustness -- 'eXperimental', 'eXtraneous', or 'eXtraordinary'
  Functionality for Robust Statistics.  Hence methods which are not well established,
  often related to methods in package 'robustbase'.  Amazingly, 'BACON()', originally by
  Billor, Hadi, and Velleman (2000) <doi:10.1016/S0167-9473(99)00101-2>
  has become established in places.  The "barrow wheel" `rbwheel()` is from
  Stahel and Mächler (2009) <doi:10.1111/j.1467-9868.2009.00706.x>.
	"""
	
	cran = "robustX" 

	version("1.2-7", md5="c1cac17c3789e471b3e69aff46528bbf")

	depends_on("r-robustbase@0.92.3:", type=("build", "run"))
