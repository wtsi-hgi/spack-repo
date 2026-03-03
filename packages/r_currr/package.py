# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCurrr(RPackage):
	"""Apply Mapping Functions in Frequent Saving

	Implementations of the family of map() functions with frequent saving of the intermediate results. The contained functions let you start the evaluation of the iterations where you stopped  (reading the already evaluated ones from cache), and work with the currently evaluated iterations while remaining ones are running in a background job. Parallel computing is also easier with the workers parameter.
	"""
	
	homepage = "https://github.com/MarcellGranat/currr"
	cran = "currr" 

	version("0.1.2", md5="aeb4385e414cf5f1ac0d1fee6b884abb")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-pacman", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-clisymbols", type=("build", "run"))
	depends_on("r-job", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
