# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHfr(RPackage):
	"""Estimate Hierarchical Feature Regression Models

	Provides functions for the estimation, plotting, predicting and cross-validation of hierarchical feature regression models as described in Pfitzinger (2021) <arXiv:2107.04831>.
	"""
	
	cran = "hfr" 

	version("0.6.2", md5="4404e49aa44380f9349489c352275543")

	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
