# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrmix(RPackage):
	"""Quantile Regression Mixture Models

	Implements the robust algorithm for fitting finite mixture models based on quantile regression proposed by Emir et al., 2017 (unpublished).
	"""
	
	cran = "qrmix" 

	version("0.9.0", md5="2ac560705fc8714cfdb90b2068d20e6a")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
