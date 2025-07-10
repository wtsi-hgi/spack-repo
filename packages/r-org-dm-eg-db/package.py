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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.Dm.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.Dm.eg.db/org.Dm.eg.db_3.18.0.tar.gz"]

	version("3.18.0", sha256="46693c745ac637135baa35a229abe7124d099c9b250902829684dac1ade719d8")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

