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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GeneSelectMMD_2.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GeneSelectMMD/GeneSelectMMD_2.46.0.tar.gz"]

    version("2.52.0", tag="RELEASE_3_21")
	version("2.46.0", sha256="2ab522ca336f948b56e8811640eeb0f67ef12dc79bf924083408b755906fa925")

	depends_on("r@2.13.2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
