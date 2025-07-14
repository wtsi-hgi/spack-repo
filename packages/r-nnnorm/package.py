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

    version("2.72.0", tag="RELEASE_3_21")
	version("2.66.0", sha256="d6ca0b553097dd9e40a6e8f1b431f8e6ac30b71289c7c0b5a4cddc5a1d43c471")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
