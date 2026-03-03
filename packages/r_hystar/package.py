# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHystar(RPackage):
	"""Fit the Hysteretic Threshold Autoregressive Model

	Estimate parameters of the hysteretic threshold autoregressive
    (HysTAR) model, using conditional least squares.
    In addition, you can generate time series data from the HysTAR model.
    For details, see Li, Guan, Li and Yu (2015) <doi:10.1093/biomet/asv017>.
	"""
	
	homepage = "https://github.com/daandejongen/hystar/"
	cran = "hystar" 

	version("1.0.0", md5="32e599e22ad6eb4a4cf05c5fd767e159")

	depends_on("r-rcpp", type=("build", "run"))
