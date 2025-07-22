# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbioportaldata(RPackage):
	"""Exposes and makes available data from the cBioPortal web resources

	The cBioPortalData R package accesses study datasets from the cBio Cancer Genomics Portal. It accesses the data either from the pre-packaged zip / tar files or from the API interface that was recently implemented by the cBioPortal Data Team. The package can provide data in either tabular format or with MultiAssayExperiment object that uses familiar Bioconductor data representations.
	"""
	
	bioc = "cBioPortalData" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cBioPortalData_2.14.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cBioPortalData/cBioPortalData_2.14.2.tar.gz"]

	version("2.20.0", tag="RELEASE_3_21")
	version("2.14.2", sha256="06038da253b5f99d40955b99dc8f64d9bd8bdd0e81b934ae02d8ffb896b967ad")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-anvil@1.7.1:", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-biocfilecache@1.5.3:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-raggedexperiment", type=("build", "run"))
	depends_on("r-rtcgatoolbox@2.19.7:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tcgautils@1.9.4:", type=("build", "run"))
