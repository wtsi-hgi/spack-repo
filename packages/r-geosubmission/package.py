# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeosubmission(RPackage):
	"""Prepares microarray data for submission to GEO

	Helps to easily submit a microarray dataset and the associated sample information to GEO by preparing a single file for upload (direct deposit).
	"""
	
	bioc = "GEOsubmission" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GEOsubmission_1.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GEOsubmission/GEOsubmission_1.54.0.tar.gz"]

	version("1.60.0", tag="RELEASE_3_21")
	version("1.54.0", sha256="1c5354f541ec5a0e12f56d9c7a1ab24fd908f14560dae54588740266a7c72c0e")

	depends_on("r-affy", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
