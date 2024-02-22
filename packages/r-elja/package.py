# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElja(RPackage):
	"""Linear, Logistic and Generalized Linear Models Regressions for
the EnvWAS/EWAS Approach

	Tool for Environment-Wide Association Studies (EnvWAS / EWAS) 
    which are repeated analysis. It includes three functions. One function for
    linear regression, a second for logistic regression and a last one for
    generalized linear models.
	"""
	
	homepage = "https://github.com/EHMarwan/Elja"
	cran = "Elja" 

	version("1.0.0", md5="3f4822548aed3a7128cf5183e2a65684")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
