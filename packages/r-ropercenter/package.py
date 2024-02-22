# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRopercenter(RPackage):
	"""Reproducible Data Retrieval from the Roper Center Data Archive

	Reproducible, programmatic retrieval of datasets from the
    Roper Center data archive.  The Roper Center for Public Opinion
    Research <https://ropercenter.cornell.edu> maintains the largest 
    archive of public opinion data in existence, but researchers using
    these datasets are caught in a bind.  The Center's terms and conditions
    bar redistribution of downloaded datasets, but to ensure that one's 
    work can be reproduced, assessed, and built upon by others, one must
    provide access to the raw data one employed.  The `ropercenter`
    package cuts this knot by providing registered users with programmatic,
    reproducible access to Roper Center datasets from within R.
	"""
	
	homepage = "https://github.com/fsolt/ropercenter"
	cran = "ropercenter" 

	version("0.3.2", md5="d081e38e72e5bbd232aefce79c759a2d")

	depends_on("r-rselenium", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-netstat", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
