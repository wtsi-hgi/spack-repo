# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKegglincs(RPackage):
	"""Visualize all edges within a KEGG pathway and overlay LINCS data

	See what is going on 'under the hood' of KEGG pathways by explicitly re-creating the pathway maps from information obtained from KGML files.
	"""
	
	bioc = "KEGGlincs" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/KEGGlincs_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/KEGGlincs/KEGGlincs_1.28.0.tar.gz"]

	version("1.28.0", md5="9ef4b8d4652560f3e9fddb3209adb0dd")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-kodata", type=("build", "run"))
	depends_on("r-hgu133a-db", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))
