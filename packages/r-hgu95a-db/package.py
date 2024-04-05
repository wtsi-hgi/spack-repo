# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95aDb(RPackage):
	"""Affymetrix Affymetrix HG_U95A Array annotation data (chip hgu95a)

	Affymetrix Affymetrix HG_U95A Array annotation data (chip hgu95a) assembled using data from public repositories
	"""
	
	bioc = "hgu95a.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95a.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95a.db/hgu95a.db_3.13.0.tar.gz"]

	version("3.13.0", md5="b228ec0eded3ba9bccf033c2fff8f7b8")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

