# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133abarcodevecs(RPackage):
	"""hgu133a data for barcode

	Data used by the barcode package for microarrays of type hgu133a.
	"""
	
	bioc = "hgu133abarcodevecs" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/hgu133abarcodevecs_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/hgu133abarcodevecs/hgu133abarcodevecs_1.40.0.tar.gz"]

	version("1.40.0", md5="4a6ec67e649f7ca004242fd860f79521")

	depends_on("r@2.10:", type=("build", "run"))

	# experiment