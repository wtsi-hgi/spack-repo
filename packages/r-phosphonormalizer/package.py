# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhosphonormalizer(RPackage):
	"""Compensates for the bias introduced by median normalization in

	It uses the overlap between enriched and non-enriched datasets to compensate for the bias introduced in global phosphorylation after applying median normalization.
	"""
	
	bioc = "phosphonormalizer"

	version("1.32.0", commit="a1abba5c9165c6bc88a993ba6002651ecf122f60")
	version("1.26.0", commit="87d2bf4fbe1b78a50607d5a9a229e8e875003d55")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
