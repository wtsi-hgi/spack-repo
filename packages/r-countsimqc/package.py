# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCountsimqc(RPackage):
	"""Compare Characteristic Features of Count Data Sets

	countsimQC provides functionality to create a comprehensive report comparing a broad range of characteristics across a collection of count matrices. One important use case is the comparison of one or more synthetic count matrices to a real count matrix, possibly the one underlying the simulations. However, any collection of count matrices can be compared.
	"""
	
	homepage = "https://github.com/csoneson/countsimQC"
	bioc = "countsimQC"

	version("1.26.0", commit="88022ecb2b4078259d1d75c19a3dd1e64b74c515")
	version("1.20.0", commit="7089dc07e446accba2c5d8ce1a595ebdb497c775")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rmarkdown@2.5:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-deseq2@1.16:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-genomeinfodbdata", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-randtests", type=("build", "run"))
	depends_on("r-ragg", type=("build", "run"))
