# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrasp2db(RPackage):
	"""grasp2db, sqlite wrap of GRASP 2.0

	grasp2db, sqlite wrap of NHLBI GRASP 2.0, an extended GWAS catalog.
	"""
	
	bioc = "grasp2db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/grasp2db_1.1.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/grasp2db/grasp2db_1.1.0.tar.gz"]

	version("1.1.0", md5="3fc90fc7c99e7da51dcbb687fd2d5515")

	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))

	# annotation