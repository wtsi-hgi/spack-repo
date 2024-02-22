# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsvy(RPackage):
	"""Import and Export CSV Data with a YAML Metadata Header

	Support for import from and export to the CSVY file format. CSVY is a file format that combines the simplicity of CSV (comma-separated values) with the metadata of other plain text and binary formats (JSON, XML, Stata, etc.) by placing a YAML header on top of a regular CSV.
	"""
	
	homepage = "https://github.com/leeper/csvy"
	cran = "csvy" 

	version("0.3.0", md5="9197de7a51e397c7644746aafa08c56a")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
