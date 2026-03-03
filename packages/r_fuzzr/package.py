# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzr(RPackage):
	"""Fuzz-Test R Functions

	Test function arguments with a wide array of inputs, and produce
  reports summarizing messages, warnings, errors, and returned values.
	"""
	
	homepage = "https://github.com/mdlincoln/fuzzr"
	cran = "fuzzr" 

	version("0.2.2", md5="17b32ca44deb6ff19fa997101ed5dea3")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
