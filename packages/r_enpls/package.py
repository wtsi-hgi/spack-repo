# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnpls(RPackage):
	"""Ensemble Partial Least Squares Regression

	An algorithmic framework for measuring feature importance,
    outlier detection, model applicability domain evaluation,
    and ensemble predictive modeling with (sparse)
    partial least squares regressions.
	"""
	
	homepage = "https://nanx.me/enpls/"
	cran = "enpls" 

	version("6.1", md5="e2ee9d4c9df2d84671e06d932aaa97c5")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-spls", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
