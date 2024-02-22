# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaex10sttranscriptclusterDb(RPackage):
	"""Affymetrix raex10 annotation data (chip raex10sttranscriptcluster)

	Affymetrix raex10 annotation data (chip raex10sttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "raex10sttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/raex10sttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/raex10sttranscriptcluster.db/raex10sttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="3a0c511a1073c67172770bc3e4b842b5")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

	# annotation