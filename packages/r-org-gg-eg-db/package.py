# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgGgEgDb(RPackage):
	"""Genome wide annotation for Chicken

	Genome wide annotation for Chicken, primarily based on mapping using Entrez Gene identifiers.
	"""
	
	bioc = "org.Gg.eg.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/org.Gg.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/org.Gg.eg.db/org.Gg.eg.db_3.18.0.tar.gz"]

	version("3.18.0", md5="4ebcbfb0baeee3332a2a07aeae2402a9")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation