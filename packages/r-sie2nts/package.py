# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSie2nts(RPackage):
	"""Sieve Methods for Non-Stationary Time Series

	We provide functions for estimation and inference of locally-stationary time series using the sieve methods and bootstrapping procedure. In addition, it also contains functions to generate Daubechies and Coiflet wavelet by Cascade algorithm and to process data visualization.
	"""
	
	cran = "Sie2nts" 

	version("0.1.0", md5="0080acd5f5fc439c257d20fea88d43a8")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
