# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCelegansDb(RPackage):
	"""Affymetrix Affymetrix Celegans Array annotation data (chip celegans)

	Affymetrix Affymetrix Celegans Array annotation data (chip celegans) assembled using data from public repositories
	"""
	
	bioc = "celegans.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/celegans.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/celegans.db/celegans.db_3.13.0.tar.gz"]

	version("3.13.0", md5="3cfa9df5a81ef538a890ed8c5d5a98ad")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-ce-eg-db@3.13:", type=("build", "run"))

	# annotation