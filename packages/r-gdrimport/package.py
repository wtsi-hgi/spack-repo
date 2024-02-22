# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdrimport(RPackage):
	"""Package for handling the import of dose-response data

	The package is a part of the gDR suite. It helps to prepare raw drug response data for downstream processing. It mainly contains helper functions for importing/loading/validating dose-response data provided in different file formats.
	"""
	
	bioc = "gDRimport" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/gDRimport_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/gDRimport/gDRimport_1.0.0.tar.gz"]

	version("1.0.0", md5="0390ee6a16f21624044bc509ebdbabd1")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-bumpymatrix", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-coregx", type=("build", "run"))
	depends_on("r-pharmacogx", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-gdrutils@0.99.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
