# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTelefit(RPackage):
	"""Estimation and Prediction for Remote Effects Spatial Process
Models

	Implementation of the remote effects spatial process (RESP) model for teleconnection.  The RESP model is a geostatistical model that allows a spatially-referenced variable (like average precipitation) to be influenced by covariates defined on a remote domain (like sea surface temperatures).  The RESP model is introduced in Hewitt et al. (2018) <doi:10.1002/env.2523>.  Sample code for working with the RESP model is available at <https://jmhewitt.github.io/research/resp_example>. This material is based upon work supported by the National Science Foundation under grant number AGS 1419558. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation.
	"""
	
	cran = "telefit" 

	version("1.0.3", md5="eb09f8091d568e34fc9e928e2466fbb5")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-itertools", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-scoringrules", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-rcpp@0.12.4:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3.1:", type=("build", "run"))
