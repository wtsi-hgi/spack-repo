# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REuropepmc(RPackage):
	"""R Interface to the Europe PubMed Central RESTful Web Service.

	An R Client for the Europe PubMed Central RESTful Web Service (see
	<https://europepmc.org/RestfulWebService> for more information). It gives
	access to both metadata on life science literature and open access full
	texts. Europe PMC indexes all PubMed content and other literature sources
	including Agricola, a bibliographic database of citations to the
	agricultural literature, or Biological Patents. In addition to
	bibliographic metadata, the client allows users to fetch citations and
	reference lists. Links between life-science literature and other EBI
	databases, including ENA, PDB or ChEMBL are also accessible. No
	registration or API key is required. See the vignettes for usage
	examples."""

	cran = "europepmc"

	version("0.4.3", md5="48e0d25bac61dc2c03656cbc29774288")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
