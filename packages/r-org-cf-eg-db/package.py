# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgCfEgDb(RPackage):
	"""Genome wide annotation for Canine

	Genome wide annotation for Canine, primarily based on mapping using Entrez Gene identifiers.
	"""
	
	bioc = "org.Cf.eg.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.Cf.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.Cf.eg.db/org.Cf.eg.db_3.18.0.tar.gz"]

	version("3.18.0", sha256="d772ab3f2c8b8baacada5273ee65493c9ca1ce5d13ef3bf5f9eded821e43d231")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

