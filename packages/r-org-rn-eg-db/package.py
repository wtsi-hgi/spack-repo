# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgRnEgDb(RPackage):
	"""Genome wide annotation for Rat

	Genome wide annotation for Rat, primarily based on mapping using Entrez Gene identifiers.
	"""
	
	bioc = "org.Rn.eg.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/org.Rn.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/org.Rn.eg.db/org.Rn.eg.db_3.18.0.tar.gz"]

	version("3.18.0", md5="1ff92cec0fc2cbd5b3055d1153526ce3")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation