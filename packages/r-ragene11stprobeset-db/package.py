# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRagene11stprobesetDb(RPackage):
	"""Affymetrix ragene11 annotation data (chip ragene11stprobeset)

	Affymetrix ragene11 annotation data (chip ragene11stprobeset) assembled using data from public repositories
	"""
	
	bioc = "ragene11stprobeset.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ragene11stprobeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ragene11stprobeset.db/ragene11stprobeset.db_8.8.0.tar.gz"]

	version("8.8.0", sha256="4ffcf033e32ed31ce25a5e7feb38992acf581c11e62ada2475f841f30aa0a7f7")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

