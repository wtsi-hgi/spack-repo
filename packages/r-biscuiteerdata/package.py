# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiscuiteerdata(RPackage):
	"""Data Package for Biscuiteer

	Contains default datasets used by the Bioconductor package biscuiteer.
	"""
	
	bioc = "biscuiteerData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/biscuiteerData_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/biscuiteerData/biscuiteerData_1.16.0.tar.gz"]

	version("1.16.0", md5="9610f1ea2c2e8303acbb0b52204f8d3e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))

	# experiment