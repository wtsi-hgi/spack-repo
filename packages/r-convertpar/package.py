# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConvertpar(RPackage):
	"""Estimating IRT Parameters via Machine Learning Algorithms

	A tool to estimate IRT item parameters (2 PL) using CTT-based item statistics from small samples via artificial neural networks and regression trees.
	"""
	
	cran = "ConvertPar" 

	version("0.1", md5="266fc2d8abfc924b0e137da9fed89b14")

	depends_on("r-neuralnet", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-rweka", type=("build", "run"))
