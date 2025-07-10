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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.Bt.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.Bt.eg.db/org.Bt.eg.db_3.18.0.tar.gz"]

	version("3.18.0", sha256="cc2db0bad0782754897657a77c98e4bb6b739f697c6096bc3a03719d9dbcf939")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

