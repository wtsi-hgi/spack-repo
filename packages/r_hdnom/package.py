# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdnom(RPackage):
	"""Benchmarking and Visualization Toolkit for Penalized Cox Models

	Creates nomogram visualizations for penalized Cox regression
    models, with the support of reproducible survival model building,
    validation, calibration, and comparison for high-dimensional data.
	"""
	
	homepage = "https://nanx.me/hdnom/"
	cran = "hdnom" 

	version("6.0.3", md5="b0c21024d6bc337429ef511f91e4ca69")
	version("6.0.2", md5="03798140e70f9c0846dc0c48ca782509")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-penalized", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
