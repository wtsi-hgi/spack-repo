# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixexp(RPackage):
	"""Design and Analysis of Mixture Experiments

	Functions for creating designs for mixture experiments, making ternary contour plots, and making mixture effect plots.
	"""
	
	cran = "mixexp" 

	version("1.2.7", md5="1d027e6ac0a9c861935c8561cfa36aaf")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-daewr", type=("build", "run"))
