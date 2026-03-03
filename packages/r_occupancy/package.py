# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROccupancy(RPackage):
	"""Probability Functions for Occupancy Distributions

	The classical and extended occupancy distributions occur in cases where balls are randomly allocated 
    to bins. The PDF, CDF, quantile functions, generation of random variates, and calculating 
    the first four central moments of the distributions are implemented as described in 
    O’Neill (2019) <doi:10.1080/00031305.2019.1699445>.
	"""
	
	cran = "occupancy" 

	version("1.2", md5="00ed0683aacca8934dd36dd7ac7e4192")

	depends_on("r-matrixstats", type=("build", "run"))
