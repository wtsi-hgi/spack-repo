# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCheckthat(RPackage):
	"""Intuitive Unit Testing Tools for Data Manipulation

	Provides a lightweight data validation and testing toolkit for R. 
    Its guiding philosophy is that adding code-based data checks to users' 
    existing workflow should be both quick and intuitive. The suite of 
    functions included therefore mirror the common data checks many users 
    already perform by hand or by eye. Additionally, the 'checkthat' package is 
    optimized to work within 'tidyverse' data manipulation pipelines.
	"""
	
	homepage = "https://github.com/iancero/checkthat"
	cran = "checkthat" 

	version("0.1.0", md5="bfc1a9e9f99009e855c759b83f5843e4")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-purrr@1.0.2:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
