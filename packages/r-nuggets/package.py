# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNuggets(RPackage):
	"""Extensible Data Pattern Searching Framework

	Extensible framework for
    subgroup discovery (Atzmueller (2015) <doi:10.1002/widm.1144>),
    contrast patterns (Chen (2022) <doi:10.48550/arXiv.2209.13556>),
    emerging patterns (Dong (1999) <doi:10.1145/312129.312191>) and
    association rules (Agrawal (1994) <https://www.vldb.org/conf/1994/P487.PDF>).
    Both crisp (binary) and fuzzy data are supported.
    It generates conditions in the form of elementary conjunctions, evaluates
    them on a dataset and checks the induced sub-data for interesting statistical
    properties. Currently, the package searches for implicative association rules
    and conditional correlations (Hájek (1978) <doi:10.1007/978-3-642-66943-9>).
    A user-defined function may be defined to evaluate on each generated
    condition to search for custom patterns.
	"""
	
	cran = "nuggets" 

	version("1.0.2", md5="e562ffd189cb8139240334f2e258a72c")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
