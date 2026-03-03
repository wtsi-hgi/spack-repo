# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPepr(RPackage):
	"""Reading Portable Encapsulated Projects

	A PEP, or Portable Encapsulated Project, is a dataset that 
    subscribes to the PEP structure for organizing metadata. It is written using
    a simple YAML + CSV format, it is your one-stop solution to metadata 
    management across data analysis environments. This package reads this 
    standardized project configuration structure into R. 
    Described in Sheffield et al. (2021) <doi:10.1093/gigascience/giab077>.
	"""
	
	cran = "pepr" 

	version("0.5.0", md5="08e6f5f4cbf4d75c54f4c968f6e587b1")

	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
