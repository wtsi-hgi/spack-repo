# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgXlEgDb(RPackage):
	"""Genome wide annotation for Xenopus

	Genome wide annotation for Xenopus, primarily based on mapping using Entrez Gene identifiers.
	"""
	
	bioc = "org.Xl.eg.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.Xl.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.Xl.eg.db/org.Xl.eg.db_3.18.0.tar.gz"]

	version("3.18.0", md5="bbea76a4373d8b51048029b83c591aca")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

