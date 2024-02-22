# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoisemodel(RPackage):
	"""Noise Models for Classification Datasets

	Implementation of models for the controlled introduction of errors in 
	classification datasets. This package contains the noise models described in 
	Saez (2022) <doi:10.3390/math10203736> that allow corrupting class labels, 
	attributes and both simultaneously.
	"""
	
	cran = "noisemodel" 

	version("1.0.2", md5="c86cfc269780c32d08a40bb8d589894b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-classint", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-extdist", type=("build", "run"))
	depends_on("r-lsr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rsnns", type=("build", "run"))
	depends_on("r-c50", type=("build", "run"))
