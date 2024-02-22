# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHta20transcriptclusterDb(RPackage):
	"""Affymetrix hta20 annotation data (chip hta20transcriptcluster)

	Affymetrix hta20 annotation data (chip hta20transcriptcluster) assembled using data from public repositories
	"""
	
	bioc = "hta20transcriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hta20transcriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hta20transcriptcluster.db/hta20transcriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="9debbc190cc5f9f0ad97fbc452fe7025")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

	# annotation