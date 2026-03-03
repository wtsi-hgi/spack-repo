# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigstep(RPackage):
	"""Stepwise Selection for Large Data Sets

	Selecting linear and generalized linear models for large data sets
    using modified stepwise procedure and modern selection criteria (like
    modifications of Bayesian Information Criterion). Selection can be 
    performed on data which exceed RAM capacity. Bogdan et al., (2004)
    <doi:10.1534/genetics.103.021683>.
	"""
	
	homepage = "https://github.com/pmszulc/bigstep"
	cran = "bigstep" 

	version("1.1.1", md5="08393b6f96e0b86dc00ea103cb8d2a0d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-speedglm", type=("build", "run"))
