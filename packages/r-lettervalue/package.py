# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLettervalue(RPackage):
	"""Computing Letter Values

	Letter Values for the course Exploratory Data Analysis at Federal University of Bahia (Brazil). The approach implemented in the package is presented in the textbook of Tukey  (1977) <ISBN: 978-0201076165>.
	"""
	
	cran = "lettervalue" 

	version("0.2.1", md5="b8d45fbc9b81c3a7bbf40c0fa51bece8")

	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
