# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRagene21sttranscriptclusterDb(RPackage):
	"""Affymetrix ragene21 annotation data (chip ragene21sttranscriptcluster)

	Affymetrix ragene21 annotation data (chip ragene21sttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "ragene21sttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ragene21sttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ragene21sttranscriptcluster.db/ragene21sttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", sha256="0add06685e3db0c8e392108332a7d0ebff23b4e1491b3179bef3e01fef001792")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

