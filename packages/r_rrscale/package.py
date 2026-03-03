# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrscale(RPackage):
	"""Robust Re-Scaling to Better Recover Latent Effects in Data

	Non-linear transformations of data to better discover latent effects. Applies a sequence of three transformations (1) a Gaussianizing transformation, (2) a Z-score transformation, and (3) an outlier removal transformation. A publication describing the method has the following citation: Gregory J. Hunt, Mark A. Dane, James E. Korkola, Laura M. Heiser & Johann A. Gagnon-Bartsch (2020) "Automatic Transformation and Integration to Improve Visualization and Discovery of Latent Effects in Imaging Data", Journal of Computational and Graphical Statistics, <doi:10.1080/10618600.2020.1741379>.
	"""
	
	cran = "rrscale" 

	version("1.0", md5="833a80663ca5b0b7352ed974fe127d54")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
