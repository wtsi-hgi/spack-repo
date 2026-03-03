# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxsei(RPackage):
	"""Fitting a CoxSEI Model

	Fit a CoxSEI (Cox type Self-Exciting Intensity) model to right-censored counting process data.
	"""
	
	cran = "coxsei" 

	version("0.3", md5="d00e438f982254435ca90cab9a086ed4")

