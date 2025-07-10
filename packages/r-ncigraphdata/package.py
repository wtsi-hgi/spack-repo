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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/NCIgraphData_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/NCIgraphData/NCIgraphData_1.38.0.tar.gz"]

	version("1.38.0", sha256="0694e4067b93bbbbc9afd0045ce8ac7af0a409fcc45ef04729b06aea8c5051c1")

	depends_on("r@2.10:", type=("build", "run"))

