# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApa(RPackage):
	"""Format Outputs of Statistical Tests According to APA Guidelines

	Formatter functions in the 'apa' package take the return value of a
    statistical test function, e.g. a call to chisq.test() and return a string
    formatted according to the guidelines of the APA (American Psychological
    Association).
	"""
	
	homepage = "https://github.com/dgromer/apa"
	cran = "apa" 

	version("0.3.4", md5="a633423637d387aa8897c0638e808930")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mbess", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
