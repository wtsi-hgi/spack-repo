# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeatr(RPackage):
	"""Neat Data for Presentation

	Utilities for unambiguous, neat and legible
    representation of data (date, time stamp, numbers, percentages and strings) 
    for presentation of analysis , aiming for elegance and consistency.
    The purpose of this package is to format data, that is better 
    for presentation and any automation jobs that reports numbers.
	"""
	
	cran = "neatR" 

	version("0.2.0", md5="13c6dc9d38fd5c2309343229b59320c5")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
