# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgCeEgDb(RPackage):
	"""Genome wide annotation for Worm

	Genome wide annotation for Worm, primarily based on mapping using Entrez Gene identifiers.
	"""
	
	bioc = "org.Ce.eg.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.Ce.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.Ce.eg.db/org.Ce.eg.db_3.18.0.tar.gz"]

	version("3.18.0", md5="441a5efb4649a1201b5552b14c1f1cef")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation