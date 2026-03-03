# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMigrate(RPackage):
	"""Create Credit State Migration (Transition) Matrices

	Tools to help convert credit risk data at two time points 
    into traditional credit state migration (aka, "transition") matrices.
    At a higher level, 'migrate' is intended to help an analyst understand 
    how risk moved in their credit portfolio over a time interval. 
    References to this methodology include: 
    1. Schuermann, T. (2008) <doi:10.1002/9780470061596.risk0409>.
    2. Perederiy, V. (2017) <arXiv:1708.00062>.
	"""
	
	homepage = "https://github.com/mthomas-ketchbrook/migrate"
	cran = "migrate" 

	version("0.4.0", md5="03c40c853db1b0c13c02f6cba508c460")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
