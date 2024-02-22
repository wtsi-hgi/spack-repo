# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcigraphdata(RPackage):
	"""Data for the NCIgraph software package

	Provides pathways from the NCI Pathways Database as R graph objects
	"""
	
	bioc = "NCIgraphData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/NCIgraphData_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/NCIgraphData/NCIgraphData_1.38.0.tar.gz"]

	version("1.38.0", md5="f144169473d42fafb1966986dcf15628")

	depends_on("r@2.10:", type=("build", "run"))

	# experiment