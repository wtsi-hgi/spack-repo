# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdmconnector(RPackage):
	"""Connect to an OMOP Common Data Model

	Provides tools for working with observational health data in the 
  Observational Medical Outcomes Partnership (OMOP) Common Data Model format with a pipe friendly syntax.
  Common data model database table references are stored in a single compound object along with metadata.
	"""
	
	homepage = "https://darwin-eu.github.io/CDMConnector/"
	cran = "CDMConnector" 

	version("1.3.0", md5="cfd8f80fd669e6984aef687a0a4f4709")
	version("1.3.1", md5="47c7152552b7398fa163738048875bb4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbi@0.3:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dbplyr@2.4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-waldo", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-omopgenerics@0.0.2:", type=("build", "run"))
