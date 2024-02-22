# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGiplot(RPackage):
	"""Gaussian Interval Plot (GIplot)

	The Gaussian Interval Plot (GIplot) is a pictorial representation of the mean
    and the standard deviation of a quantitative variable. It also flags 
    potential outliers (together with their frequencies) that are c standard deviations away from the mean. 
	"""
	
	cran = "GIplot" 

	version("0.1.0", md5="a8c8d83f14f357cf465bbefb86d59a3e")

