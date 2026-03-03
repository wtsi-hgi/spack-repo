# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNempi(RPackage):
	"""Inferring unobserved perturbations from gene expression data

	Takes as input an incomplete perturbation profile and differential gene expression in log odds and infers unobserved perturbations and augments observed ones. The inference is done by iteratively inferring a network from the perturbations and inferring perturbations from the network. The network inference is done by Nested Effects Models.
	"""
	
	homepage = "https://github.com/cbg-ethz/nempi/"
	bioc = "nempi" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/nempi_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/nempi/nempi_1.10.0.tar.gz"]

	version("1.10.0", md5="1180e323b8f109079a74702ef7159cda")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mnem", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-naturalsort", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-epinem", type=("build", "run"))
