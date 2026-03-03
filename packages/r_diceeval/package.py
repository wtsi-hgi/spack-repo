# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiceeval(RPackage):
	"""Construction and Evaluation of Metamodels

	Estimation, validation and prediction of models of different types : linear models, additive models, MARS,PolyMARS and Kriging.
	"""
	
	cran = "DiceEval" 

	version("1.6.1", md5="e44d0be4b4a0199953c356db26ed18f9")

	depends_on("r-dicekriging", type=("build", "run"))
