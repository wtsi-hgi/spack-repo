# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaxtoolsr(RPackage):
	"""Access Pathways from Multiple Databases Through BioPAX and Pathway Commons

	The package provides a set of R functions for interacting with BioPAX OWL files using Paxtools and the querying Pathway Commons (PC) molecular interaction database. Pathway Commons is a project by the Memorial Sloan-Kettering Cancer Center (MSKCC), Dana-Farber Cancer Institute (DFCI), and the University of Toronto. Pathway Commons databases include: BIND, BioGRID, CORUM, CTD, DIP, DrugBank, HPRD, HumanCyc, IntAct, KEGG, MirTarBase, Panther, PhosphoSitePlus, Reactome, RECON, TRANSFAC.
	"""
	
	homepage = "https://github.com/BioPAX/paxtoolsr"
	bioc = "paxtoolsr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/paxtoolsr_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/paxtoolsr/paxtoolsr_1.36.0.tar.gz"]

    version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="f050c8aea3cd37c14a8b4d1292bdb7f007f442078a8ef0e5a4286d1387f5331f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rjava@0.9.8:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("openjdk@1.6:", type=("build", "link", "run"))
