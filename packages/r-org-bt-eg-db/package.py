# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgBtEgDb(RPackage):
	"""Genome wide annotation for Bovine

	Genome wide annotation for Bovine, primarily based on mapping using Entrez Gene identifiers.
	"""
	
	bioc = "org.Bt.eg.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/org.Bt.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/org.Bt.eg.db/org.Bt.eg.db_3.18.0.tar.gz"]

	version("3.18.0", md5="23fd8017323c86930c50d596204bad54")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation