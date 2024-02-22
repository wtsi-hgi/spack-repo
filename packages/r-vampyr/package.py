# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVampyr(RPackage):
	"""Factor Analysis Controlling the Effects of Response Bias

	Vampirize the response biases from a dataset! Performs 
    factor analysis controlling the effects of social desirability
    and acquiescence using the method described in Ferrando, 
    Lorenzo-Seva & Chico (2009) <doi:10.1080/10705510902751374>.
	"""
	
	cran = "vampyr" 

	version("1.1.1", md5="9bf2febb1e1a0c2e1f47fa72d599d59a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-efa-mrfa", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-pcovr", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-fungible", type=("build", "run"))
	depends_on("r-semplot", type=("build", "run"))
