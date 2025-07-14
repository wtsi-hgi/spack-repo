# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnmix(RPackage):
	"""Quality control and analysis tools for Illumina DNA methylation BeadChip

	Tools for quanlity control, analysis and visulization of Illumina DNA methylation array data.
	"""
	
	homepage = "https://github.com/Bioconductor/ENmix"
	bioc = "ENmix"

	version("1.44.3", commit="57de9c26c0c28a08a6bc113f24941ac0b9a44ed2")
	version("1.38.01", commit="0a1ee50d9ca45e7130dd5416265bfc7801ada443")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-geneplotter", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-rpmm", type=("build", "run"))
	depends_on("r-illuminaio", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
