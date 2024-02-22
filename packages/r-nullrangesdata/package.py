# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNullrangesdata(RPackage):
	"""ExperimentHub datasets for the nullranges package

	Provides datasets for the nullranges package vignette, in particular example datasets for DNase hypersensitivity sites (DHS), CTCF binding sites, and CTCF genomic interactions. These are used to demonstrate generation of null hypothesis feature sets, either through block bootstrapping or matching, in the nullranges vignette.  For more details, see the data object man pages, and the R scripts for object construction provided within the package.
	"""
	
	bioc = "nullrangesData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/nullrangesData_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/nullrangesData/nullrangesData_1.8.0.tar.gz"]

	version("1.8.0", md5="c8b4cf63d70a2577251c03c093c014b1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-interactionset", type=("build", "run"))

	# experiment