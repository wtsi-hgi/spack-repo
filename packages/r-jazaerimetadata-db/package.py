# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJazaerimetadataDb(RPackage):
	"""A data package containing annotation data for JazaeriMetaData

	A data package containing annotation data for JazaeriMetaData assembled using data from public repositories
	"""
	
	bioc = "JazaeriMetaData.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/JazaeriMetaData.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/JazaeriMetaData.db/JazaeriMetaData.db_3.2.3.tar.gz"]

	version("3.2.3", md5="3a154a74ac2acebe3471b039c9d9a4dc")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

	# annotation