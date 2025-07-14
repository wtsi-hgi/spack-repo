# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeconvr(RPackage):
	"""Simulation and Deconvolution of Omic Profiles

	This package provides a collection of functions designed for analyzing deconvolution of the bulk sample(s) using an atlas of reference omic signature profiles and a user-selected model. Users are given the option to create or extend a reference atlas and,also simulate the desired size of the bulk signature profile of the reference cell types.The package includes the cell-type-specific methylation atlas and, Illumina Epic B5 probe ids that can be used in deconvolution. Additionally,we included BSmeth2Probe, to make mapping WGBS data to their probe IDs easier.
	"""
	
	homepage = "https://github.com/BIMSBbioinfo/deconvR"
	bioc = "deconvR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/deconvR_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/deconvR/deconvR_1.8.0.tar.gz"]

	version("1.14.0", tag="RELEASE_3_21")
	version("1.8.0", sha256="2358e1bfee30fa0164c609fdfb86101d34346a4dce7a416dfa9c6be414b7845e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-s4vectors@0.30:", type=("build", "run"))
	depends_on("r-methylkit@1.18:", type=("build", "run"))
	depends_on("r-iranges@2.26:", type=("build", "run"))
	depends_on("r-genomicranges@1.44:", type=("build", "run"))
	depends_on("r-biocgenerics@0.38:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-matrixstats@0.61:", type=("build", "run"))
	depends_on("r-e1071@1.7.9:", type=("build", "run"))
	depends_on("r-quadprog@1.5.8:", type=("build", "run"))
	depends_on("r-nnls@1.4:", type=("build", "run"))
	depends_on("r-rsq@2.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
