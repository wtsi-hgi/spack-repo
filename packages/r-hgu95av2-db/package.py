# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95av2Db(RPackage):
	"""Affymetrix Affymetrix HG_U95Av2 Array annotation data (chip hgu95av2)

	Affymetrix Affymetrix HG_U95Av2 Array annotation data (chip hgu95av2) assembled using data from public repositories
	"""
	
	bioc = "hgu95av2.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95av2.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95av2.db/hgu95av2.db_3.13.0.tar.gz"]

	version("3.13.0", sha256="ff722f64852a02bcc2c31e5329847df3cb16796c327993f1525d7c74d3aa63fe")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

