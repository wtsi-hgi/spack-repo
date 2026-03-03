# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircumplex(RPackage):
	"""Analysis and Visualization of Circular Data

	Circumplex models, which organize constructs in a circle around two 
    underlying dimensions, are popular for studying interpersonal functioning, 
    mood/affect, and vocational preferences/environments. This package provides 
    tools for analyzing and visualizing circular data, including scoring 
    functions for relevant instruments and a generalization of the bootstrapped 
    structural summary method from Zimmermann & Wright (2017) 
    <doi:10.1177/1073191115621795> and functions for creating publication-ready 
    tables and figures from the results.
	"""
	
	homepage = "https://github.com/jmgirard/circumplex"
	cran = "circumplex" 

	version("0.3.10", md5="64eb9dee8268065436aca37aaa9b3162")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-boot@1.3.18:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-ggforce@0.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-htmltable@1.13.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.11:", type=("build", "run"))
