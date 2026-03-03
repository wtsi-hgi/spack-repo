# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransomics2cytoscape(RPackage):
	"""A tool set for 3D Trans-Omic network visualization with Cytoscape

	transomics2cytoscape generates a file for 3D transomics visualization by providing input that specifies the IDs of multiple KEGG pathway layers, their corresponding Z-axis heights, and an input that represents the edges between the pathway layers. The edges are used, for example, to describe the relationships between kinase on a pathway and enzyme on another pathway. This package automates creation of a transomics network as shown in the figure in Yugi.2014 (https://doi.org/10.1016/j.celrep.2014.07.021) using Cytoscape automation (https://doi.org/10.1186/s13059-019-1758-4).
	"""
	
	bioc = "transomics2cytoscape" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/transomics2cytoscape_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/transomics2cytoscape/transomics2cytoscape_1.12.0.tar.gz"]

	version("1.12.0", md5="17325dd51ab6dfcc10dff97e98be6e91")

	depends_on("r-rcy3", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("cytoscape@3.10.0:", type=("build", "link", "run"))
