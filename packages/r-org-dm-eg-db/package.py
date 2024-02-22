# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgDmEgDb(RPackage):
	"""Genome wide annotation for Fly

	Genome wide annotation for Fly, primarily based on mapping using Entrez Gene identifiers.
	"""
	
	bioc = "org.Dm.eg.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/org.Dm.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/org.Dm.eg.db/org.Dm.eg.db_3.18.0.tar.gz"]

	version("3.18.0", md5="92577ed3bc5d76b78905169eebfebe7d")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation