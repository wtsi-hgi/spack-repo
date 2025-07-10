# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMta10probesetDb(RPackage):
	"""Affymetrix mta10 annotation data (chip mta10probeset)

	Affymetrix mta10 annotation data (chip mta10probeset) assembled using data from public repositories
	"""
	
	bioc = "mta10probeset.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mta10probeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mta10probeset.db/mta10probeset.db_8.8.0.tar.gz"]

	version("8.8.0", sha256="359e0c9be8092f956040dda5fdaaa7c5a8e721de3f0e0a7923836a9c12af4ccf")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

