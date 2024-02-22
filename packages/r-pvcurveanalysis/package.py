# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPvcurveanalysis(RPackage):
	"""Analysis of Pressure Volume Curves

	Enables the manufacturing, analysis and display of pressure volume curves. From the progression of the curves, turgor loss point, osmotic potential and apoplastic fraction can be derived. Methods adapted from Bartlett, Scoffoni and Sack (2012) <doi:10.1111/j.1461-0248.2012.01751.x>.
	"""
	
	cran = "pvcurveanalysis" 

	version("1.0.0", md5="c0d31ac8afeb0043c800761129a85e76")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
