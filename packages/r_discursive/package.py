# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscursive(RPackage):
	"""Measuring Discursive Sophistication in Open-Ended Survey
Responses

	A simple approach to measure political sophistication based on open-ended survey responses. Discursive sophistication captures the complexity of individual attitude expression by quantifying its relative size, range, and constraint. For more information on the measurement approach see: Kraft, Patrick W. 2023. "Women Also Know Stuff: Challenging the Gender Gap in Political Sophistication." American Political Science Review (forthcoming).
	"""
	
	cran = "discursive" 

	version("0.1.1", md5="148b707773cde5ba9ce8935cbc9eacb4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-stm", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
