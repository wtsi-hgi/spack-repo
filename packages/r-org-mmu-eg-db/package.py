# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgMmuEgDb(RPackage):
	"""Genome wide annotation for Rhesus

	Genome wide annotation for Rhesus, primarily based on mapping using Entrez Gene identifiers.
	"""
	
	bioc = "org.Mmu.eg.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/org.Mmu.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/org.Mmu.eg.db/org.Mmu.eg.db_3.18.0.tar.gz"]

	version("3.18.0", md5="45a35940d0d1ab91b2b262a8666afa53")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation