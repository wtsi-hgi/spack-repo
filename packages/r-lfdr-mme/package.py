# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLfdrMme(RPackage):
	"""Estimating Local False Discovery Rates Using the Method of
Moments

	Estimation of the local false discovery rate using the method of moments.
	"""
	
	cran = "LFDR.MME" 

	version("1.0", md5="40770923b28fe088e39b53ad565fe6bd")

	depends_on("r@2.14.2:", type=("build", "run"))
