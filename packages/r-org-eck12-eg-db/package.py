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
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/org.EcK12.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/org.EcK12.eg.db/org.EcK12.eg.db_3.18.0.tar.gz"]

	version("3.18.0", md5="50d3d3ca9efec212eae3a920b00750a3")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation