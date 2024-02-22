# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRagene10stprobesetDb(RPackage):
	"""Affymetrix ragene10 annotation data (chip ragene10stprobeset)

	Affymetrix ragene10 annotation data (chip ragene10stprobeset) assembled using data from public repositories
	"""
	
	bioc = "ragene10stprobeset.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/ragene10stprobeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/ragene10stprobeset.db/ragene10stprobeset.db_8.8.0.tar.gz"]

	version("8.8.0", md5="358685c380b37027a064924069b9ee40")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

	# annotation