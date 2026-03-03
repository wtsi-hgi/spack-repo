# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChicData(RPackage):
	"""ChIC package data

	This package contains annotation and metagene profile data for the ChIC package.
	"""
	
	bioc = "ChIC.data" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ChIC.data_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ChIC.data/ChIC.data_1.22.0.tar.gz"]

	version("1.22.0", md5="34b50ea53e6b5c982dc044addc68c33b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomeintervals", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-caret@6.0.78:", type=("build", "run"))

