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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ENmix_1.38.01.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ENmix/ENmix_1.38.01.tar.gz"]

	version("1.38.01", sha256="03b0aaba5716e78f7a8da53c555b1a1dbf74cf17a6182b180169dc9662a609f2")

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
