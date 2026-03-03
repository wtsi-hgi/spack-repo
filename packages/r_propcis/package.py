# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPropcis(RPackage):
	"""Various Confidence Interval Methods for Proportions

	Computes two-sample confidence intervals for single, paired and independent proportions.
	"""
	
	homepage = "https://github.com/shearer/PropCIs"
	cran = "PropCIs" 

	version("0.3-0", md5="4840669d4cf4c3d6a42fa6142d2e1450")

