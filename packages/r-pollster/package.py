# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPollster(RPackage):
	"""Calculate Crosstab and Topline Tables of Weighted Survey Data

	Calculate common types of tables for weighted survey data.
    Options include topline and (2-way and 3-way) crosstab tables of
    categorical or ordinal data as well as summary tables of weighted
    numeric variables. Optionally, include the margin of error at
    selected confidence intervals including the design effect. The
    design effect is calculated as described by 
    Kish (1965) <doi:10.1002/bimj.19680100122> beginning
    on page 257. Output takes the form of tibbles (simple data frames).
    This package conveniently handles labelled data, such as that
    commonly used by 'Stata' and 'SPSS.' Complex survey design is 
    not supported at this time. 
	"""
	
	cran = "pollster" 

	version("0.1.6", md5="4e69522c1470e59a30f8cca6cc24f906")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-labelled@2:", type=("build", "run"))
	depends_on("r-forcats@1:", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
