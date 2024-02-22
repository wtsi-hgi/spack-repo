# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcev(RPackage):
	"""Principal Component of Explained Variance

	Principal component of explained variance (PCEV) is a statistical
    tool for the analysis of a multivariate response vector. It is a dimension-
    reduction technique, similar to Principal component analysis (PCA), that seeks
    to maximize the proportion of variance (in the response vector) being explained
    by a set of covariates.
	"""
	
	homepage = "http://github.com/GreenwoodLab/pcev"
	cran = "pcev" 

	version("2.2.2", md5="97841fa06a3f69b2cdaab900de8599d4")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rmtstat", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
