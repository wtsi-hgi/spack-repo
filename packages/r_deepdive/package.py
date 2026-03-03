# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeepdive(RPackage):
	"""Deep Learning for General Purpose

	Aims to provide simple intuitive functions to create quick prototypes of artificial neural network or deep learning models. In addition novel ensemble models like 'deeptree' and 'deepforest' has been included which combines decision trees and neural network.
	"""
	
	homepage = "https://rajeshb24.github.io/deepdive/"
	cran = "deepdive" 

	version("1.0.4", md5="f431da7d96b8e30607e0cf75080c21a8")

	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-treeclust", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
