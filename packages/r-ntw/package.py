# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNtw(RPackage):
	"""Predict gene network using an Ordinary Differential Equation (ODE) based method

	This package predicts the gene-gene interaction network and identifies the direct transcriptional targets of the perturbation using an ODE (Ordinary Differential Equation) based method.
	"""
	
	bioc = "NTW"

	version("1.58.0", commit="c68d2de0db5cfb3f568b002b58788ad63905839b")
	version("1.52.0", commit="b7a6e0132fcbccc5e404f340b3579b3c3b5ab839")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
