# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLlama(RPackage):
	"""Leveraging Learning to Automatically Manage Algorithms

	Provides functionality to train and evaluate algorithm selection models for portfolios.
	"""
	
	homepage = "https://bitbucket.org/lkotthoff/llama"
	cran = "llama" 

	version("0.10.1", md5="bcaa01a66c9d3e8cff4bd601e5051b01")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mlr@2.5:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-parallelmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
