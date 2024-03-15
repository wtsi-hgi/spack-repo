# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMusMusculus(RPackage):
	"""Annotation package for the Mus.musculus object

	Contains the Mus.musculus object to access data from several related annotation packages.
	"""
	
	bioc = "Mus.musculus" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Mus.musculus_1.3.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/Mus.musculus/Mus.musculus_1.3.1.tar.gz"]

	version("1.3.1", md5="1b8defe64c2dd308a88d1ac7a4ce04b9")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-organismdbi@1.11.39:", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-txdb-mmusculus-ucsc-mm10-knowngene", type=("build", "run"))

	# annotation