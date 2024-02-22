# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRattusNorvegicus(RPackage):
	"""Annotation package for the Rattus.norvegicus object

	Contains the Rattus.norvegicus object to access data from several related annotation packages.
	"""
	
	bioc = "Rattus.norvegicus" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Rattus.norvegicus_1.3.1.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/Rattus.norvegicus/Rattus.norvegicus_1.3.1.tar.gz"]

	version("1.3.1", md5="5692fdeb0bc7f94e1db35f097cad99a9")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-organismdbi@1.11.39:", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-org-rn-eg-db", type=("build", "run"))
	depends_on("r-txdb-rnorvegicus-ucsc-rn5-refgene", type=("build", "run"))

	# annotation