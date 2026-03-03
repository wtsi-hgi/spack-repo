# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTar(RPackage):
	"""Bayesian Modeling of Autoregressive Threshold Time Series Models

	Identification and estimation of the autoregressive threshold models with Gaussian noise, as well as positive-valued time series. The package provides the identification of the number of regimes, the thresholds and the autoregressive orders, as well as the estimation of remain parameters. The package implements the methodology from the 2005 paper: Modeling Bivariate Threshold Autoregressive Processes in the Presence of Missing Data <DOI:10.1081/STA-200054435>.
	"""
	
	cran = "TAR" 

	version("1.0", md5="5390b09c30cb13355f4b49311c5f35e6")

	depends_on("r-mvtnorm", type=("build", "run"))
