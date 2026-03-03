# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatdap(RPackage):
	"""Categorical Data Analysis Program Package

	Categorical data analysis by AIC. The methodology is described in
 Sakamoto (1992) <ISBN 978-0-7923-1429-5>.
	"""
	
	cran = "catdap" 

	version("1.3.7", md5="758b3858df3715f4ddd9a832ecf12339")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
