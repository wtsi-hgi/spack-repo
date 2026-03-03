# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNnnorm(RPackage):
	"""Spatial and intensity based normalization of cDNA microarray data based on robust neural nets

	This package allows to detect and correct for spatial and intensity biases with two-channel microarray data. The normalization method implemented in this package is based on robust neural networks fitting.
	"""
	
	homepage = "http://bioinformaticsprb.med.wayne.edu/tarca/"
	bioc = "nnNorm" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/nnNorm_2.66.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/nnNorm/nnNorm_2.66.0.tar.gz"]

	version("2.66.0", md5="f6e41106fc2afb44568c00dce1a36670")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
