# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDipsaus(RPackage):
	"""A Dipping Sauce for Data Analysis and Visualizations

	Works as an "add-on" to packages like 'shiny', 'future', as well as 
    'rlang', and provides utility functions. Just like dipping sauce adding 
    flavors to potato chips or pita bread, 'dipsaus' for data analysis and 
    visualizations adds handy functions and enhancements to popular packages. 
    The goal is to provide simple solutions that are frequently asked for 
    online, such as how to synchronize 'shiny' inputs without freezing the app,
    or how to get memory size on 'Linux' or 'MacOS' system. The enhancements 
    roughly fall into these four categories: 1. 'shiny' input widgets; 2. 
    high-performance computing using the 'future' package; 3. 
    modify R calls and convert among numbers, strings, and other objects. 4. 
    utility functions to get system information such like CPU chip-set, memory 
    limit, etc.
	"""
	
	homepage = "https://github.com/dipterix/dipsaus"
	cran = "dipsaus" 

	version("0.2.8", md5="c0f9ca75aa4663bb0eaa480564318160")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-fastmap@1.1:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-rstudioapi@0.11:", type=("build", "run"))
