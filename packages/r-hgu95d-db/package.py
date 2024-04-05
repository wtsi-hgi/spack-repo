# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95dDb(RPackage):
	"""Affymetrix Affymetrix HG_U95D Array annotation data (chip hgu95d)

	Affymetrix Affymetrix HG_U95D Array annotation data (chip hgu95d) assembled using data from public repositories
	"""
	
	bioc = "hgu95d.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95d.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95d.db/hgu95d.db_3.13.0.tar.gz"]

	version("3.13.0", md5="90ecf383640f6ab7314fa1babcdd5a0b")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

