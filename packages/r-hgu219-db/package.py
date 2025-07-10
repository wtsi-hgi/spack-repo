# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu219Db(RPackage):
	"""Affymetrix Human Genome 219 Plate annotation data (chip hgu219)

	Affymetrix Human Genome 219 Plate annotation data (chip hgu219) assembled using data from public repositories
	"""
	
	bioc = "hgu219.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu219.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu219.db/hgu219.db_3.2.3.tar.gz"]

	version("3.2.3", sha256="64847ad0392b2e1f2a79eb24cc90e5359e42c2c8bf265d1ec7d2dd443ee567fb")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

