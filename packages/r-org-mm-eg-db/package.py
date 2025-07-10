# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgMmEgDb(RPackage):
	"""Genome wide annotation for Mouse

	Genome wide annotation for Mouse, primarily based on mapping using Entrez Gene identifiers.
	"""
	
	bioc = "org.Mm.eg.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.Mm.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.Mm.eg.db/org.Mm.eg.db_3.18.0.tar.gz"]

	version("3.18.0", sha256="41ab6c87f6a8c2a13718f7b1d1bdfde37dcaf61bc34915cc3a8e2348a96b6544")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

