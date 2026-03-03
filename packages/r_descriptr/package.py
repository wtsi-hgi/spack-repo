# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDescriptr(RPackage):
	"""Generate Descriptive Statistics

	Generate descriptive statistics such as measures of location,
    dispersion, frequency tables, cross tables, group summaries and multiple
    one/two way tables. 
	"""
	
	homepage = "https://descriptr.rsquaredacademy.com/"
	cran = "descriptr" 

	version("0.5.2", md5="7930559901bf7a2917c2e5b76a389e9f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
