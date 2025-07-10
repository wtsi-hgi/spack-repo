# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProda(RPackage):
	"""Differential Abundance Analysis of Label-Free Mass Spectrometry Data

	Account for missing values in label-free mass spectrometry data without imputation. The package implements a probabilistic dropout model that ensures that the information from observed and missing values are properly combined. It adds empirical Bayesian priors to increase power to detect differentially abundant proteins.
	"""
	
	homepage = "https://github.com/const-ae/proDA"
	bioc = "proDA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/proDA_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/proDA/proDA_1.16.0.tar.gz"]

	version("1.16.0", sha256="7787a07fa4c1a70c4770ed7764b879e053076812d0469577b41e277c1505fa23")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
