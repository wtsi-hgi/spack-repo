# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrictionless(RPackage):
	"""Read and Write Frictionless Data Packages

	Read and write Frictionless Data Packages. A 'Data Package'
    (<https://specs.frictionlessdata.io/data-package/>) is a simple container
    format and standard to describe and package a collection of (tabular) data. 
    It is typically used to publish FAIR 
    (<https://www.go-fair.org/fair-principles/>) and open datasets.
	"""
	
	homepage = "https://github.com/frictionlessdata/frictionless-r"
	cran = "frictionless" 

	version("1.0.3", md5="dfad94efed132f5aec80c1967d22bb6b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr@2.1:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
