# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCprr(RPackage):
	"""Functions for Working with Danish CPR Numbers

	Calculate date of birth, age, and gender, and generate anonymous
    sequence numbers from CPR numbers.
    <https://en.wikipedia.org/wiki/Personal_identification_number_(Denmark)>.
	"""
	
	homepage = "http://github.com/anhoej/cprr"
	cran = "cprr" 

	version("0.2.0", md5="74c795907a351f3b6baac464baa62729")

	depends_on("r@3.1:", type=("build", "run"))
