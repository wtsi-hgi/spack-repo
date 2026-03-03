# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidydr(RPackage):
	"""Unify Dimensionality Reduction Results

	Dimensionality reduction (DR) is widely used in many domain for analyzing and visualizing high-dimensional data. 'tidydr' provides uniform output and is compatible with multiple methods, including 'prcomp', 'mds', 'Rtsne'. etc.
	"""
	
	homepage = "https://github.com/YuLab-SMU/tidydr/"
	cran = "tidydr" 

	version("0.0.5", md5="8cf7108a8128408b487e096ed4babbda")

	depends_on("r-ggfun", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
