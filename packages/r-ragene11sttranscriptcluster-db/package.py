# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRagene11sttranscriptclusterDb(RPackage):
	"""Affymetrix ragene11 annotation data (chip ragene11sttranscriptcluster)

	Affymetrix ragene11 annotation data (chip ragene11sttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "ragene11sttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ragene11sttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ragene11sttranscriptcluster.db/ragene11sttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="f7fbe318547f911b520415a90b3440e9")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

	# annotation