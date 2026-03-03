# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdiwr(RPackage):
	"""DDI with R

	Useful functions for various DDI (Data Documentation Initiative)
    related inputs and outputs. Converts data files to and from DDI, SPSS,
    Stata, SAS, R and Excel, including user declared missing values.
	"""
	
	homepage = "https://github.com/dusadrian/DDIwR"
	cran = "DDIwR" 

	version("0.18", md5="c886965edf2389165cb1edf49c800157")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-admisc@0.33:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-declared@0.23:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
