# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgSsEgDb(RPackage):
	"""Genome wide annotation for Pig

	Genome wide annotation for Pig, primarily based on mapping using Entrez Gene identifiers.
	"""
	
	bioc = "org.Ss.eg.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.Ss.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.Ss.eg.db/org.Ss.eg.db_3.18.0.tar.gz"]

	version("3.18.0", md5="f9b32c76d23f9195df7a7eb6529f3340")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

