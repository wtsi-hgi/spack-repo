# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenesummary(RPackage):
	"""RefSeq Gene Summaries

	This package provides long description of genes collected from the RefSeq database. The text in "COMMENT" section started with "Summary" is extracted as the description of the gene. The long text descriptions can be used for analysis such as text mining.
	"""
	
	homepage = "https://github.com/jokergoo/GeneSummary"
	bioc = "GeneSummary" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/GeneSummary_0.99.6.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/GeneSummary/GeneSummary_0.99.6.tar.gz"]

	version("0.99.6", tag="RELEASE_3_21")
	version("0.99.6", sha256="e5d6ead968d2cd401c510ac0ee30b9dff1caceed54f36a38cb4e01b06476ca40")

	depends_on("r@4:", type=("build", "run"))

