# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFr(RPackage):
	"""Frictionless Standards

	A "tabular-data-resource" (<https://specs.frictionlessdata.io/tabular-data-resource/>) is a simple format to describe a singular tabular data resource such as a CSV file. It includes support both for metadata such as author and title and a schema to describe the data, for example the types of the fields/columns in the data. Create a tabular-data-resource by providing a data.frame and specifying metadata. Write and read tabular-data-resources to and from disk. 
	"""
	
	homepage = "https://github.com/cole-brokamp/fr"
	cran = "fr" 

	version("0.5.1", md5="03ca3c8c269c124350d15b605276ef17")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-s7@0.1.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
