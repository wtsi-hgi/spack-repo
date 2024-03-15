# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrnn(RPackage):
	"""Quantile Regression Neural Network

	Fit quantile regression neural network models with optional
    left censoring, partial monotonicity constraints, generalized additive
    model constraints, and the ability to fit multiple non-crossing quantile
    functions following Cannon (2011) <doi:10.1016/j.cageo.2010.07.005>
    and Cannon (2018) <doi:10.1007/s00477-018-1573-6>.
	"""
	
	cran = "qrnn" 

	version("2.1.1", md5="dc2a527654c8b325dcc0fb3245682b39")

