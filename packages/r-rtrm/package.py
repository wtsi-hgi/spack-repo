# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtrm(RPackage):
	"""Identification of Transcriptional Regulatory Modules from Protein-Protein Interaction Networks

	rTRM identifies transcriptional regulatory modules (TRMs) from protein-protein interaction networks.
	"""
	
	homepage = "https://github.com/ddiez/rTRM"
	bioc = "rTRM" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rTRM_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rTRM/rTRM_1.40.0.tar.gz"]

	version("1.40.0", md5="2804488949a044166efe737d4e25d9ac")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph@1:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
