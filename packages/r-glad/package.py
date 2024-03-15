# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlad(RPackage):
	"""Gain and Loss Analysis of DNA

	Analysis of array CGH data : detection of breakpoints in genomic profiles and assignment of a status (gain, normal or loss) to each chromosomal regions identified.
	"""
	
	homepage = "http://bioinfo.curie.fr"
	bioc = "GLAD" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GLAD_2.66.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GLAD/GLAD_2.66.0.tar.gz"]

	version("2.66.0", md5="f222e07624fb8b1c4780a4960b0f2008")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-aws", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
