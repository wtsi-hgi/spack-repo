# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyxl(RPackage):
	"""Read Untidy Excel Files

	Imports non-tabular from Excel files into R.  Exposes cell content,
    position and formatting in a tidy structure for further manipulation.
    Tokenizes Excel formulas.  Supports '.xlsx' and '.xlsm' via the embedded
    'RapidXML' C++ library <https://rapidxml.sourceforge.net>.  Does not support
    '.xlsb' or '.xls'.
	"""
	
	homepage = "https://github.com/nacnudus/tidyxl"
	cran = "tidyxl" 

	version("1.0.10", md5="d97f2d616c19c23072194ef290903c17")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-piton@1:", type=("build", "run"))
