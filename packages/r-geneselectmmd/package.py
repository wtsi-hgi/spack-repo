# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneselectmmd(RPackage):
	"""Gene selection based on the marginal distributions of gene profiles that characterized by a mixture of three-component multivariate distributions

	Gene selection based on a mixture of marginal distributions.
	"""
	
	bioc = "GeneSelectMMD" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GeneSelectMMD_2.46.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GeneSelectMMD/GeneSelectMMD_2.46.0.tar.gz"]

	version("2.46.0", md5="dd6cd07bbe095fca03ce4b134c1507b8")

	depends_on("r@2.13.2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
