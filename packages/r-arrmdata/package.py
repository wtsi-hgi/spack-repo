# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArrmdata(RPackage):
	"""Example dataset for normalization of Illumina 450k Methylation data

	Raw Beta values from 36 samples across 3 groups from Illumina 450k methylation arrays
	"""
	
	bioc = "ARRmData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ARRmData_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ARRmData/ARRmData_1.38.0.tar.gz"]

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="4793554365ad2319db8b96314d4cbf3b725c0e09edd9f8975dc126bee7619042")

	depends_on("r@3:", type=("build", "run"))

