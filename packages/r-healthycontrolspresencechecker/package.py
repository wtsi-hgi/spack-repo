# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHealthycontrolspresencechecker(RPackage):
	"""Dowloads A Gene Expression Dataset From GEO And Checks If It Contains Data Of Healthy Controls Or Not

	A function that reads in the GEO accession code of a gene expression dataset, retrieves its data from GEO, and checks if data of healthy controls are present in the dataset. It returns true if healthy controls data are found, and false otherwise. GEO: Gene Expression Omnibus. ID: identifier code. The GEO datasets are downloaded from the URL <https://ftp.ncbi.nlm.nih.gov/geo/series/>.
	"""
	
	homepage = "https://github.com/davidechicco/healthyControlsPresenceChecker"
	bioc = "healthyControlsPresenceChecker" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/healthyControlsPresenceChecker_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/healthyControlsPresenceChecker/healthyControlsPresenceChecker_1.6.0.tar.gz"]

	version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="55c47ef108b255911cd60dd92f4efe2c276a0dd755e6e1114bbd01873907f788")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-geneexpressionfromgeo", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))

