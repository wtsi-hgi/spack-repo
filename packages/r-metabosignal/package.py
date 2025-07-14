# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabosignal(RPackage):
	"""MetaboSignal: a network-based approach to overlay and explore metabolic and signaling KEGG pathways

	MetaboSignal is an R package that allows merging, analyzing and customizing metabolic and signaling KEGG pathways. It is a network-based approach designed to explore the topological relationship between genes (signaling- or enzymatic-genes) and metabolites, representing a powerful tool to investigate the genetic landscape and regulatory networks of metabolic phenotypes.
	"""
	
	bioc = "MetaboSignal"

	version("1.38.0", commit="2b03e8ee50a8a86272fa952c8d9dc82bd35db483")
	version("1.32.1", commit="76ac054f1355d139536bf17127ae93f949a2ebd4")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
	depends_on("r-hpar", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-ensdb-hsapiens-v75", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-mwastools", type=("build", "run"))
	depends_on("r-mygene", type=("build", "run"))
