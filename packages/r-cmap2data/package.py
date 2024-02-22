# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmap2data(RPackage):
	"""Connectivity Map (version 2) Data

	Data package which provides default drug profiles for the DrugVsDisease package as well as associated gene lists and data clusters used by the DrugVsDisease package.
	"""
	
	bioc = "cMap2data" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/cMap2data_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/cMap2data/cMap2data_1.38.0.tar.gz"]

	version("1.38.0", md5="c5ecbc59a690426c6def7feb720e1a7d")

	depends_on("r@2.10:", type=("build", "run"))

	# experiment