# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcheck(RPackage):
	"""QC Pipeline and Data Analysis Tools for High-Dimensional Illumina mRNA Expression Data

	QC pipeline and data analysis tools for high-dimensional Illumina mRNA expression data.
	"""
	
	bioc = "iCheck" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iCheck_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iCheck/iCheck_1.32.0.tar.gz"]

    version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="d8f3313ea9acf0ff834f3cff568ccaf8f5c224055bbd913025543ecd142f8ef4")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-lumi", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-geneselectmmd", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
