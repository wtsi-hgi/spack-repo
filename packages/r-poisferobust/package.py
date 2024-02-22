# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoisferobust(RPackage):
	"""Poisson Fixed Effects Robust

	Computation of robust standard errors of Poisson fixed effects 
    models, following Wooldridge (1999).
	"""
	
	homepage = "https://bitbucket.org/ew-btb/poisson-fe-robust"
	cran = "poisFErobust" 

	version("2.0.0", md5="6cdc65a783523b38d82dc44f87b10160")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-glmmml@1:", type=("build", "run"))
