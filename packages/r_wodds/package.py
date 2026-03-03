# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWodds(RPackage):
	"""Calculates Whisker Odds

	Descriptive statistics for large data tend to be low resolution on the tails. 
    Whisker Odds generate a table of descriptive statistics for large data. This is the same as
    letter-values, but with an alternative naming of depths which allow for depths beyond 26. For 
    a reference to letter-values see 'Heike Hofmann' and 'Hadley Wickham' and 'Karen Kafadar' (2017) <doi:10.1080/10618600.2017.1305277>.
	"""
	
	homepage = "https://github.com/alexhallam/wodds"
	cran = "wodds" 

	version("0.1.0", md5="4659580a4962120eeb3750e37db87fbb")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
