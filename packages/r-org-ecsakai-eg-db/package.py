# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgEcsakaiEgDb(RPackage):
	"""Genome wide annotation for E coli strain Sakai

	Genome wide annotation for E coli strain Sakai, primarily based on mapping using Entrez Gene identifiers.
	"""
	
	bioc = "org.EcSakai.eg.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/org.EcSakai.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/org.EcSakai.eg.db/org.EcSakai.eg.db_3.18.0.tar.gz"]

	version("3.18.0", md5="3f26ffa55ce30fc8caa64f826207ac61")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation