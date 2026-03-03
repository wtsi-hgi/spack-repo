# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCureplots(RPackage):
	"""CURE (Cumulative Residual) Plots

	Creates 'ggplot2' Cumulative Residual (CURE) plots to check the goodness-of-fit of a count model; or the tables to create a customized version. A dataset of crashes in Washington state is available for illustrative purposes.
	"""
	
	homepage = "https://github.com/gbasulto/cureplots"
	cran = "cureplots" 

	version("1.1.0", md5="8b97beaeaa9d66e8276fb55f0ff78810")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
