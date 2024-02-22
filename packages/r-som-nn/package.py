# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSomNn(RPackage):
	"""Topological k-NN Classifier Based on Self-Organising Maps

	A topological version of k-NN: An abstract model is build
             as 2-dimensional self-organising map. Samples of unknown
             class are predicted by mapping them on the SOM and analysing
             class membership of neurons in the neighbourhood.
	"""
	
	cran = "som.nn" 

	version("1.1.0", md5="b2dc934fbf5554bdf8fcdd1217b633d7")

	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-kohonen", type=("build", "run"))
	depends_on("r-som", type=("build", "run"))
