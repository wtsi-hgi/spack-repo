# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROffsetreg(RPackage):
	"""An Extension of 'Tidymodels' Supporting Offset Terms

	Extend the 'tidymodels' ecosystem <https://www.tidymodels.org/> to
    enable the creation of predictive models with offset terms. Models with 
    offsets are most useful when working with count data or when fitting an
    adjustment model on top of an existing model with a prior expectation. 
    The former situation is common in insurance where data is often weighted by
    exposures. The latter is common in life insurance where industry mortality 
    tables are often used as a starting point for setting assumptions.
	"""
	
	homepage = "https://github.com/mattheaphy/offsetreg/"
	cran = "offsetreg" 

	version("1.0.0", md5="229b0e8dcee0520d0b54c8ee1896c1e6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r-poissonreg", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
