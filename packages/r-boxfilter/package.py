# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoxfilter(RPackage):
	"""Filter Noisy Data

	Noise filter based on determining the proportion of neighboring points. A false point will be rejected if it has only few neighbors, but accepted if the proportion of neighbors in a rectangular frame is high. The size of the rectangular frame as well as the cut-off value, i.e. of a minimum proportion of neighbor-points, may be supplied or can be calculated automatically. Originally designed for the cleaning of heart rates, but suitable for filtering any slowly-changing physiological variable.For more information see Signer (2010)<doi:10.1111/j.2041-210X.2009.00010.x>.
	"""
	
	cran = "boxfilter" 

	version("0.2", md5="62f1f135f1df7d975cbcc1c744928c53")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
