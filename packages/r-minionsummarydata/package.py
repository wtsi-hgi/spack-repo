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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/minionSummaryData_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/minionSummaryData/minionSummaryData_1.32.0.tar.gz"]

	version("1.32.0", sha256="da4513dec9b2aa8fb1cc48570fcb889116682787ac8f782cf626c55ee2396fde")

	depends_on("r@3.2:", type=("build", "run"))

