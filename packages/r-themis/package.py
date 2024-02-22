# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThemis(RPackage):
	"""Extra Recipes Steps for Dealing with Unbalanced Data

	A dataset with an uneven number of cases in each class is
    said to be unbalanced. Many models produce a subpar performance on
    unbalanced datasets. A dataset can be balanced by increasing the
    number of minority cases using SMOTE 2011 <arXiv:1106.1813>,
    BorderlineSMOTE 2005 <doi:10.1007/11538059_91> and ADASYN 2008
    <https://ieeexplore.ieee.org/document/4633969>. Or by decreasing the
    number of majority cases using NearMiss 2003
    <https://www.site.uottawa.ca/~nat/Workshop2003/jzhang.pdf> or Tomek
    link removal 1976 <https://ieeexplore.ieee.org/document/4309452>.
	"""
	
	homepage = "https://github.com/tidymodels/themis"
	cran = "themis" 

	version("1.0.2", md5="8f13545a8a8d475f3323e75dd40a66d3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-recipes@1.0.4:", type=("build", "run"))
	depends_on("r-gower", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-generics@0.1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rose", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-hardhat", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
