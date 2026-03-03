# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFqar(RPackage):
	"""Floristic Quality Assessment Tools for R

	Tools for downloading and analyzing floristic quality assessment data. 
  See Freyman et al. (2015) <doi:10.1111/2041-210X.12491> for more information 
  about floristic quality assessment and the associated database.  
	"""
	
	homepage = "https://github.com/equitable-equations/fqar/"
	cran = "fqar" 

	version("0.5.1", md5="c2c5b7b17e5a8569d8a712016a677362")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
