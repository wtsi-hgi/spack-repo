# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgop(RPackage):
	"""Aggregation Operators and Preordered Sets

	Tools supporting multi-criteria and group decision making,
    including variable number of criteria, by means of
    aggregation operators, spread measures,
    fuzzy logic connectives, fusion functions,
    and preordered sets. Possible applications include,
    but are not limited to, quality management, scientometrics,
    software engineering, etc.
	"""
	
	homepage = "https://github.com/gagolews/agop/"
	cran = "agop" 

	version("0.2.4", md5="fca44d79177a284dec0e6c50acf0cd3a")

	depends_on("r@3:", type=("build", "run"))
