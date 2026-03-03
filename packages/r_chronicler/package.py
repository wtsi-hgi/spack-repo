# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChronicler(RPackage):
	"""Add Logging to Functions

	Decorate functions to make them return enhanced output. The enhanced output consists in an object of type
  'chronicle' containing the result of the function applied to its arguments, as well as a log detailing when the function
  was run, what were its inputs, what were the errors (if the function failed to run) and other useful information.
  Tools to handle decorated functions are included, such as a forward pipe operator that makes chaining decorated functions possible.
	"""
	
	cran = "chronicler" 

	version("0.2.2", md5="ed23518bee313d1c67d5d069dd663124")
	version("0.2.1", md5="5ecff09bc12a0392d2f44ab024330035")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-diffobj", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-maybe", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
