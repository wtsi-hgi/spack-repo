# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRagene21stprobesetDb(RPackage):
	"""Affymetrix ragene21 annotation data (chip ragene21stprobeset)

	Affymetrix ragene21 annotation data (chip ragene21stprobeset) assembled using data from public repositories
	"""
	
	bioc = "ragene21stprobeset.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/ragene21stprobeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/ragene21stprobeset.db/ragene21stprobeset.db_8.8.0.tar.gz"]

	version("8.8.0", md5="6451885f99ce3873d5d4dbacdf968181")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

	# annotation