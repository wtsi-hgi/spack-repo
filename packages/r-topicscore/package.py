# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopicscore(RPackage):
	"""The Topic SCORE Algorithm to Fit Topic Models

	Provides implementation of the "Topic SCORE" algorithm that is
	     proposed by Tracy Ke and Minzhe Wang. The singular value decomposition
	     step is optimized through the usage of svds() function in 'RSpectra'
	     package, on a 'dgRMatrix' sparse matrix. Also provides a column-wise
	     error measure in the word-topic matrix A, and an algorithm for
	     recovering the topic-document matrix W given A and D based on
	     quadratic programming.
		The details about the techniques are explained in the paper "A new SVD approach to optimal topic estimation" by Tracy Ke and Minzhe Wang (2017) <arXiv:1704.07016>.
	"""
	
	cran = "TopicScore" 

	version("0.0.1", md5="f6d304b3dba85e1799d514b0ad692d6f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
