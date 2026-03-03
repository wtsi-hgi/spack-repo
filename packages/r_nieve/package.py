# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNieve(RPackage):
	"""Miscellaneous Utilities for Extreme Value Analysis

	Provides utility functions and objects for Extreme Value
    Analysis. These include probability functions with their exact
    derivatives w.r.t. the parameters that can be used for estimation
    and inference, even with censored observations. The
    transformations exchanging the two parameterizations of Peaks Over
    Threshold (POT) models: Poisson-GP and Point-Process are also
    provided with their derivatives.
	"""
	
	homepage = "https://github.com/yvesdeville/nieve/"
	cran = "nieve" 

	version("0.1.3", md5="ec889a6adfc7699e564b67964dcc2843")

