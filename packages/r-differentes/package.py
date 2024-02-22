# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDifferentes(RPackage):
	"""Computation of TES-Based Cell Differentiation Trees

	Computes the ATM (Attractor Transition Matrix) structure and
    the tree-like structure describing the cell differentiation process
    (based on the Threshold Ergodic Set concept introduced by Serra and
    Villani), starting from the Boolean networks with synchronous updating
    scheme of the 'BoolNet' R package. TESs (Threshold Ergodic Sets) are
    the mathematical abstractions that represent the different cell types
    arising during ontogenesis. TESs and the powerful model of biological
    differentiation based on Boolean networks to which it belongs have
    been firstly described in "A Dynamical Model of Genetic Networks for
    Cell Differentiation" Villani M, Barbieri A, Serra R (2011) A
    Dynamical Model of Genetic Networks for Cell Differentiation. PLOS ONE
    6(3): e17703.
	"""
	
	cran = "diffeRenTES" 

	version("0.3.2", md5="5a8a5155421ec5af2eae97d53af53ce8")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-boolnet", type=("build", "run"))
	depends_on("r-dot", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
