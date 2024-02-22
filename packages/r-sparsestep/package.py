# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsestep(RPackage):
	"""SparseStep Regression

	Implements the SparseStep model for solving regression
    problems with a sparsity constraint on the parameters. The SparseStep
    regression model was proposed in Van den Burg, Groenen, and Alfons (2017)
    <arXiv:1701.06967>. In the model, a regularization term is added to the
    regression problem which approximates the counting norm of the parameters.
    By iteratively improving the approximation a sparse solution to the
    regression problem can be obtained.  In this package both the standard
    SparseStep algorithm is implemented as well as a path algorithm which uses
    golden section search to determine solutions with different values for the
    regularization parameter.
	"""
	
	homepage = "https://github.com/GjjvdBurg/SparseStep"
	cran = "sparsestep" 

	version("1.0.1", md5="85dabe62be8ab045164e9b06ef3b069f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix@1.0.6:", type=("build", "run"))
