# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinst(RPackage):
	"""Data Preprocessing, Binning for Classification and Regression

	Various supervised and unsupervised binning tools
    including using entropy, recursive partition methods
    and clustering.
	"""
	
	homepage = "https://github.com/jules-and-dave/binst"
	cran = "binst" 

	version("0.2.1", md5="ebaedce562fa3d233a79792a4a2b7d74")

	depends_on("r-rpart", type=("build", "run"))
