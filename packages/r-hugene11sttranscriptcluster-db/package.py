# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHugene11sttranscriptclusterDb(RPackage):
	"""Affymetrix hugene11 annotation data (chip hugene11sttranscriptcluster)

	Affymetrix hugene11 annotation data (chip hugene11sttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "hugene11sttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hugene11sttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hugene11sttranscriptcluster.db/hugene11sttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", sha256="94f763f43f410f9c9d7b3c64151d21d5033358d8d4340debdbd8bbe14322467c")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

