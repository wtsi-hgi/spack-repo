# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdhs(RPackage):
	"""API Client and Dataset Management for the Demographic and Health
Survey (DHS) Data

	Provides a client for (1) querying the DHS API for survey indicators
  and metadata (<https://api.dhsprogram.com/#/index.html>), (2) identifying surveys
  and datasets for analysis, (3) downloading survey datasets from the DHS website,
  (4) loading datasets and associate metadata into R, and (5) extracting variables
  and combining datasets for pooled analysis.
	"""
	
	homepage = "https://docs.ropensci.org/rdhs/"
	cran = "rdhs" 

	version("0.8.1", md5="44076856f5e4cab7c9e2e0dc8b445ccd")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-brio", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-storr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-qdapregex", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-iotools", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
