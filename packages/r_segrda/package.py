# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSegrda(RPackage):
	"""Modeling Non-Continuous Linear Responses of Ecological Data

	Tools for modeling non-continuous linear responses of ecological communities to environmental data. The package is straightforward through three steps: (1) data ordering (function OrdData()), (2) split-moving-window analysis (function SMW()) and (3) piecewise redundancy analysis (function pwRDA()). Relevant references include Cornelius and Reynolds (1991) <doi:10.2307/1941559> and Legendre and Legendre (2012, ISBN: 9780444538697).
	"""
	
	homepage = "https://github.com/DaniloCVieira/segRDA"
	cran = "segRDA" 

	version("1.0.2", md5="b65c71305600b48beb639d1fb6755b3b")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-vegan@2.4:", type=("build", "run"))
