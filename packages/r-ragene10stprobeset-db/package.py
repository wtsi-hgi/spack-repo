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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ragene10stprobeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ragene10stprobeset.db/ragene10stprobeset.db_8.8.0.tar.gz"]

	version("8.8.0", sha256="683956662775944b2f26902385e4541de281cdad77f2406f139e07fc4da34892")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

