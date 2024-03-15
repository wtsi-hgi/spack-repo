# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsics(RPackage):
	"""Automatic Statistical Identification in Complex Spectra

	With a set of pure metabolite reference spectra, ASICS quantifies concentration of metabolites in a complex spectrum. The identification of metabolites is performed by fitting a mixture model to the spectra of the library with a sparse penalty. The method and its statistical properties are described in Tardivel et al. (2017) <doi:10.1007/s11306-017-1244-5>.
	"""
	
	bioc = "ASICS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ASICS_2.18.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ASICS/ASICS_2.18.1.tar.gz"]

	version("2.18.1", md5="f71374e7472244d5c1bcd44ab0406e01")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pepsnmr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-ropls", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
