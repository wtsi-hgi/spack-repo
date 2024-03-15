# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSticsrfiles(RPackage):
	"""Read and Modify 'STICS' Input/Output Files

	Manipulating input and output files of the 'STICS' crop
    model. Files are either 'JavaSTICS' XML files or text files used by
    the model 'fortran' executable. Most basic functionalities are reading
    or writing parameter names and values in both XML or text input files,
    and getting data from output files.  Advanced functionalities include
    XML files generation from XML templates and/or spreadsheets, or text
    files generation from XML files by using 'xslt' transformation.
	"""
	
	homepage = "https://github.com/SticsRPacks/SticsRFiles"
	cran = "SticsRFiles" 

	version("1.2.0", md5="feb0a6efce04dd0e8087d8ae429d40ce")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-xslt", type=("build", "run"))
