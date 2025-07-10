# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95bDb(RPackage):
	"""Affymetrix Affymetrix HG_U95B Array annotation data (chip hgu95b)

	Affymetrix Affymetrix HG_U95B Array annotation data (chip hgu95b) assembled using data from public repositories
	"""
	
	bioc = "hgu95b.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95b.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95b.db/hgu95b.db_3.13.0.tar.gz"]

	version("3.13.0", sha256="fb41ec27e0a67347b485cd4879c916dfa6af674afcc99d1ad5b167c70bd14b3f")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

