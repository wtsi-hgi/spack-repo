# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinionsummarydata(RPackage):
	"""Summarised MinION sequencing data published by Ashton et al. 2015

	Summarised MinION sequencing data for Salmonella Typhi published by Ashton et al. in 2015. Three replicate runs are each provided as Fast5Summary objects.
	"""
	
	bioc = "minionSummaryData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/minionSummaryData_1.32.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/minionSummaryData/minionSummaryData_1.32.0.tar.gz"]

	version("1.32.0", md5="1679c45541b2d76094c3894abe9c011d")

	depends_on("r@3.2:", type=("build", "run"))

	# experiment