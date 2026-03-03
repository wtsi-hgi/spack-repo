# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobiomedasim(RPackage):
	"""Microbiome Differential Abundance Simulation

	A toolkit for simulating differential microbiome data designed for longitudinal analyses. Several functional forms may be specified for the mean trend. Observations are drawn from a multivariate normal model. The objective of this package is to be able to simulate data in order to accurately compare different longitudinal methods for differential abundance.
	"""
	
	homepage = "https://github.com/williazo/microbiomeDASim"
	bioc = "microbiomeDASim" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/microbiomeDASim_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/microbiomeDASim/microbiomeDASim_1.16.0.tar.gz"]

	version("1.16.0", md5="9ddf99ab393766f7bcb9dee13b3707f9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-metagenomeseq", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
