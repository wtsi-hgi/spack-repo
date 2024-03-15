# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM6aboost(RPackage):
	"""m6Aboost

	This package can help user to run the m6Aboost model on their own miCLIP2 data. The package includes functions to assign the read counts and get the features to run the m6Aboost model. The miCLIP2 data should be stored in a GRanges object. More details can be found in the vignette.
	"""
	
	homepage = "https://github.com/ZarnackGroup/m6Aboost"
	bioc = "m6Aboost" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/m6Aboost_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/m6Aboost/m6Aboost_1.8.0.tar.gz"]

	version("1.8.0", md5="17bd39bcc17e45a0bb22be3e2e15c533")

	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-adabag", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
