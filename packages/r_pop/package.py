# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPop(RPackage):
	"""A Flexible Syntax for Population Dynamic Modelling

	Population dynamic models underpin a range of analyses and applications in ecology and epidemiology. The various approaches for analysing population dynamics models (MPMs, IPMs, ODEs, POMPs, PVA) each require the model to be defined in a different way. This makes it difficult to combine different modelling approaches and data types to solve a given problem. 'pop' aims to provide a flexible and easy to use common interface for constructing population dynamic models and enabling to them to be fitted and analysed in lots of different ways.
	"""
	
	cran = "pop" 

	version("0.1", md5="775d30aa0315b002328f7508c9ff0115")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
