# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuitor(RPackage):
	"""Selecting the number of mutational signatures through cross-validation

	An unsupervised cross-validation method to select the optimal number of mutational signatures. A data set of mutational counts is split into training and validation data.Signatures are estimated in the training data and then used to predict the mutations in the validation data.
	"""
	
	bioc = "SUITOR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SUITOR_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SUITOR/SUITOR_1.4.0.tar.gz"]

	version("1.4.0", md5="5f4a5ea607ef7551025cf8b425d20bc7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
