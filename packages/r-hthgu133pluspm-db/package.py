# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHthgu133pluspmDb(RPackage):
	"""Affymetrix Affymetrix HT_HG-U133_Plus_PM Array annotation data (chip hthgu133pluspm)

	Affymetrix Affymetrix HT_HG-U133_Plus_PM Array annotation data (chip hthgu133pluspm) assembled using data from public repositories
	"""
	
	bioc = "hthgu133pluspm.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hthgu133pluspm.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hthgu133pluspm.db/hthgu133pluspm.db_3.13.0.tar.gz"]

	version("3.13.0", md5="b0b3cb0174608d5705ae6c80dac02e3c")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

	# annotation