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

	version("1.14.0", commit="2f0fed757a4a9299f89011d87b8f19f6a250440a")
	version("1.8.0", commit="b4405bebf29c6d132b781aa9ac3dc603c5f38558")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-interactionset", type=("build", "run"))

