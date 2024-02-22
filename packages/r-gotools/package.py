# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGotools(RPackage):
	"""Functions for Gene Ontology database

	Wraper functions for description/comparison of oligo ID list using Gene Ontology database
	"""
	
	bioc = "goTools" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/goTools_1.76.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/goTools/goTools_1.76.0.tar.gz"]

	version("1.76.0", md5="a91344726dcce37779380a18f6e9bc1d")

	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
