# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplingin(RPackage):
	"""Dynamic Survey Sampling Solutions

	A robust solution employing both systematic and PPS
    (Probability Proportional to Size) sampling methods, ensuring a
    methodical and representative selection of data.  Seamlessly allocate
    predetermined allocations to smaller levels. Kish, L. (1965)
    <https://books.google.co.id/books?id=xiZmAAAAIAAJ>.
	"""
	
	cran = "samplingin" 

	version("1.0.6", md5="f1fd49de049b329c24024620ed755e83")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
