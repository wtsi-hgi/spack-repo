# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantpsyc(RPackage):
	"""Quantitative Psychology Tools

	Contains tools useful for data screening, testing
        moderation (Cohen et. al. 2003)<doi:10.4324/9780203774441>, 
        mediation (MacKinnon et. al. 2002)<doi:10.1037/1082-989x.7.1.83> 
        and estimating power (Murphy & Myors 2014)<ISBN:9781315773155>.
	"""
	
	cran = "QuantPsyc" 

	version("1.6", md5="4f2911168144718476a27389c4b19407")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
