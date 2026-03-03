# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNnbenchmark(RPackage):
	"""Datasets and Functions to Benchmark Neural Network Packages

	Datasets and functions to benchmark (convergence, speed, ease of use) R packages dedicated to regression with neural networks (no classification in this version). The templates for the tested packages are available in the R, R Markdown and HTML formats at <https://github.com/pkR-pkR/NNbenchmarkTemplates> and <https://theairbend3r.github.io/NNbenchmarkWeb/index.html>. The submitted article to the R-Journal can be read at <https://www.inmodelia.com/gsoc2020.html>.
	"""
	
	homepage = "https://github.com/pkR-pkR/NNbenchmark"
	cran = "NNbenchmark" 

	version("3.2.0", md5="a70bc3c59d9b742378d93f32c2d512f8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-pkgload", type=("build", "run"))
