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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/raex10sttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/raex10sttranscriptcluster.db/raex10sttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", sha256="289bfb04f5cc618d10e34a9ba605d1df76f287f0bc55f63864b8ecde44db8bf2")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

