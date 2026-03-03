# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiopn(RPackage):
	"""Simulation of deterministic and stochastic biochemical reaction
networks using Petri Nets

	
  bioPN is a package suited to perform simulation of deterministic and stochastic systems of biochemical reaction
  networks.
  Models are defined using a subset of Petri Nets, in a way that is close at how chemical reactions
  are defined.
  For deterministic solutions, bioPN creates the associated system of differential equations "on the fly", and
  solves it with a Runge Kutta Dormand Prince 45 explicit algorithm.
  For stochastic solutions, bioPN offers variants of Gillespie algorithm, or SSA.
  For hybrid deterministic/stochastic,
  it employs the Haseltine and Rawlings algorithm, that partitions the system in fast and slow reactions.
  bioPN algorithms are developed in C to achieve adequate performance.
	"""
	
	cran = "bioPN" 

	version("1.2.0", md5="a6686916274879a55ed249883f08b4ad")

