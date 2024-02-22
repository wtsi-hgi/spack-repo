# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChangepointtests(RPackage):
	"""Change Point Tests for Joint Distributions and Copulas

	Change point tests for joint distributions and copulas using pseudo-observations with multipliers or bootstrap. The processes used here have been defined in Bucher, Kojadinovic, Rohmer & Segers <doi:10.1016/j.jmva.2014.07.012> and Nasri & Remillard <doi:10.1016/j.jmva.2019.03.002>.
	"""
	
	cran = "changepointTests" 

	version("0.1.5", md5="375b36a03c77bf25c7d0a8e0a4f1f1f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
