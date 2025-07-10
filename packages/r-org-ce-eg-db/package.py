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

	version("3.18.0", sha256="b8b06a6ebac8ea36f643d6dfb3f6a486a7d4a20561a1bb74eb424de3d7ca4bbb")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

