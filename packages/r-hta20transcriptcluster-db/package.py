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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hta20transcriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hta20transcriptcluster.db/hta20transcriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", sha256="70680ab930d4290431c312449e0ab6b46f933d55c61012e903baefbaae07a92f")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

