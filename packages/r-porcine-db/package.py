# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPorcineDb(RPackage):
	"""Affymetrix Affymetrix Porcine Array annotation data (chip porcine)

	Affymetrix Affymetrix Porcine Array annotation data (chip porcine) assembled using data from public repositories
	"""
	
	bioc = "porcine.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/porcine.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/porcine.db/porcine.db_3.13.0.tar.gz"]

	version("3.13.0", md5="4a86b3e696d267dca673b4e9276d6368")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-ss-eg-db@3.13:", type=("build", "run"))

	# annotation