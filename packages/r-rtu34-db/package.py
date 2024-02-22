# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtu34Db(RPackage):
	"""Affymetrix Affymetrix RT_U34 Array annotation data (chip rtu34)

	Affymetrix Affymetrix RT_U34 Array annotation data (chip rtu34) assembled using data from public repositories
	"""
	
	bioc = "rtu34.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/rtu34.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/rtu34.db/rtu34.db_3.13.0.tar.gz"]

	version("3.13.0", md5="f46c4763627f1a9e00cdc9d0af8c5f2e")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

	# annotation