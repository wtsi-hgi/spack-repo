# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSolartime(RPackage):
	"""Utilities Dealing with Solar Time Such as Sun Position and Time
of Sunrise

	Provide utilities to work with solar time, 
  i.e. where noon is exactly when sun culminates.
  Provides functions for computing sun position and times of sunrise and sunset.
	"""
	
	homepage = "https://github.com/bgctw/solartime"
	cran = "solartime" 

	version("0.0.2", md5="d885ba7d86351c8186738f042cb90bba")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
