# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpedinstabr(RPackage):
	"""Estimation of the Relative Importance of Factors Affecting
Species Distribution Based on Stability Concept

	From output files obtained from the software 'ModestR', the relative contribution of factors to explain species distribution is depicted using several plots. A global geographic raster file for each environmental variable may be also obtained with the mean relative contribution, considering all species present in each raster cell, of the factor to explain species distribution. Finally, for each variable it is also possible to compare the frequencies of any variable obtained in the cells where the species is present with the frequencies of the same variable in the cells of the extent.
	"""
	
	cran = "SPEDInstabR" 

	version("2.2", md5="1fb913f9e6cf639c6c1db08d41702480")

	depends_on("r@3.1.1:", type=("build", "run"))
