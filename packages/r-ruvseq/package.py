# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRuvseq(RPackage):
	"""Remove Unwanted Variation from RNA-Seq Data

	This package implements the remove unwanted variation (RUV) methods of Risso et al. (2014) for the normalization of RNA-Seq read counts between samples.
	"""
	
	homepage = "https://github.com/drisso/RUVSeq"
	bioc = "RUVSeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RUVSeq_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RUVSeq/RUVSeq_1.36.0.tar.gz"]

	version("1.36.0", sha256="e2027b287cae301ccb26b742dd1830a42b0eb45a552323cea119d7adf97b7e11")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-edaseq@1.99.1:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
