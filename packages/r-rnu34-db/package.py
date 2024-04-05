# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnu34Db(RPackage):
	"""Affymetrix Affymetrix RN_U34 Array annotation data (chip rnu34)

	Affymetrix Affymetrix RN_U34 Array annotation data (chip rnu34) assembled using data from public repositories
	"""
	
	bioc = "rnu34.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rnu34.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rnu34.db/rnu34.db_3.13.0.tar.gz"]

	version("3.13.0", md5="7345817f2f26270779d2409b8a17a5bd")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

