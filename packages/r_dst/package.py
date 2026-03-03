# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDst(RPackage):
	"""Using the Theory of Belief Functions

	Using the Theory of Belief Functions for evidence calculus. Basic probability assignments, or mass functions, can be defined on the subsets of a set of possible values and combined. A mass function can be extended to a larger frame. Marginalization, i.e. reduction to a smaller frame can also be done. These features can be combined to analyze small belief networks and take into account situations where information cannot be satisfactorily described by probability distributions.
	"""
	
	cran = "dst" 

	version("1.5.2", md5="04ed463f19135cf5e8ed66aa56650a12")

	depends_on("r@2.10:", type=("build", "run"))
