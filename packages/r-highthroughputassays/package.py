# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighthroughputassays(RPackage):
	"""Using Bioconductor with High Throughput Assays

	The workflow illustrates use of the flow cytometry packages to load, transform and visualize the flow data and gate certain populations in the dataset. The workflow loads the `flowCore`, `flowStats` and `flowWorkspace` packages and its dependencies.  It loads the ITN data with 15 samples, each of which includes, in addition to FSC and SSC, 5 fluorescence channels: CD3, CD4, CD8, CD69 and HLADR.
	"""
	
	homepage = "https://www.bioconductor.org/help/workflows/highthroughputassays/"
	bioc = "highthroughputassays" 
	urls = ["https://www.bioconductor.org/packages/release/workflows/src/contrib/highthroughputassays_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/workflows/src/contrib/Archive/highthroughputassays/highthroughputassays_1.26.0.tar.gz"]

	version("1.26.0", md5="03d7477f8db26efff92737a67ed6ec5c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowstats", type=("build", "run"))
	depends_on("r-flowworkspace", type=("build", "run"))

	# workflow