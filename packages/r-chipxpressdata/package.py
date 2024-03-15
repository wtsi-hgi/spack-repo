# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipxpressdata(RPackage):
	"""ChIPXpress Pre-built Databases

	Contains pre-built mouse (GPL1261) and human (GPL570) database of gene expression profiles to be used for ChIPXpress ranking.
	"""
	
	bioc = "ChIPXpressData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ChIPXpressData_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ChIPXpressData/ChIPXpressData_1.40.0.tar.gz"]

	version("1.40.0", md5="029086a630df9533dedea4babd28f0d7")

	depends_on("r-bigmemory", type=("build", "run"))

	# experiment