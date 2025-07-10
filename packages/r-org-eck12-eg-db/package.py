# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgEck12EgDb(RPackage):
	"""Genome wide annotation for E coli strain K12

	Genome wide annotation for E coli strain K12, primarily based on mapping using Entrez Gene identifiers.
	"""
	
	bioc = "org.EcK12.eg.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.EcK12.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.EcK12.eg.db/org.EcK12.eg.db_3.18.0.tar.gz"]

	version("3.18.0", sha256="ac1ac06065ba24d21b734e3322d3f3982db7a88105125af6679c26620dd8988a")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

