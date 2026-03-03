# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCir(RPackage):
	"""Centered Isotonic Regression and Dose-Response Utilities

	Isotonic regression (IR) and its improvement: centered isotonic regression (CIR). CIR is recommended in particular with small samples. Also, interval estimates for both, and additional utilities such as plotting dose-response data. For dev version and change history, see GitHub assaforon/cir.
	"""
	
	cran = "cir" 

	version("2.3.1", md5="f8009261e7c39d4304b802b617b25c28")

