# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdmir(RPackage):
	"""Identification of Dysregulated MiRNAs Based on MiRNA-MiRNA
Interaction Network

	A systematic biology tool was developed to identify dysregulated miRNAs via a miRNA-miRNA interaction network. 'IDMIR' first constructed a weighted miRNA interaction network through integrating miRNA-target interaction information, molecular function data from Gene Ontology (GO) database and gene transcriptomic data in specific-disease context, and then, it used a network propagation algorithm on the network to identify significantly dysregulated miRNAs.
	"""
	
	cran = "IDMIR" 

	version("0.1.0", md5="59b6818a23ebc205d75f8e397645f9c6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-egg", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
