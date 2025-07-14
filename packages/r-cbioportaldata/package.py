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

	version("2.20.0", commit="e2964c093d2b83eef9b28bb4a2c86153b1bbbf04")
	version("2.14.2", commit="3d59ad61bbaa88fee972001afdd10fbf9eb55172")

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
