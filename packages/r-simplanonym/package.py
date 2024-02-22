# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplanonym(RPackage):
	"""Consistent Anonymisation Across Datasets

	A simple function that anonymises a list of variables
    in a consistent way: anonymised factors are not recycled and
    the same original levels receive the same anonymised factor
    even if located in different datasets.
	"""
	
	homepage = "https://github.com/dkgaraujo/simplanonym"
	cran = "simplanonym" 

	version("0.1.0", md5="06062b57f3578dc0803ff5cf167bcaaf")

	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-forcats@0.5.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
