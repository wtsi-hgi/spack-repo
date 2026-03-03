# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgbm(RPackage):
	"""LS-TreeBoost and LAD-TreeBoost for Gene Regulatory Network
Reconstruction

	Provides an implementation of Regularized LS-TreeBoost & LAD-TreeBoost algorithm for Regulatory Network inference from any type of expression data (Microarray/RNA-seq etc).
	"""
	
	cran = "RGBM" 

	version("1.0-11", md5="b6c1ad08c2e2d6588e58bfabb7506ed2")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
