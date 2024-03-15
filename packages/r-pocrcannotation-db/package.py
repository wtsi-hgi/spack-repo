# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPocrcannotationDb(RPackage):
	"""A package containing metadata for POCRC arrays

	A package containing metadata for POCRC arrays assembled using data from public repositories
	"""
	
	bioc = "POCRCannotation.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/POCRCannotation.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/POCRCannotation.db/POCRCannotation.db_3.2.3.tar.gz"]

	version("3.2.3", md5="da1d4dacc5fffb9c5dfea55649974aa5")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

	# annotation