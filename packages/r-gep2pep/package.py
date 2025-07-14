# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGep2pep(RPackage):
	"""Creation and Analysis of Pathway Expression Profiles (PEPs)

	Pathway Expression Profiles (PEPs) are based on the expression of pathways (defined as sets of genes) as opposed to individual genes. This package converts gene expression profiles to PEPs and performs enrichment analysis of both pathways and experimental conditions, such as "drug set enrichment analysis" and "gene2drug" drug discovery analysis respectively.
	"""
	
	bioc = "gep2pep" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/gep2pep_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/gep2pep/gep2pep_1.22.0.tar.gz"]

	version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="405094998efa1bc4a73c9ac60466138717ac7a725dd0fb738bcbce6ea4443a55")

	depends_on("r-repo@2.1.1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
