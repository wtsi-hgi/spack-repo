# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPantarhei(RPackage):
	"""Plots Sankey Diagrams

	Sankey diagrams are a powerfull and visually attractive way
  to visualize the flow of conservative substances through a system.
  They typically consists of a network of nodes, and fluxes between them,
  where the total balance in each internal node is 0, i.e. input equals output.
  Sankey diagrams are typically used to display energy systems, material flow accounts etc.
  Unlike so-called alluvial plots, Sankey diagrams also allow for cyclic flows:
  flows originating from a single node can, either direct or indirect, contribute to the input of that same node.
  This package, named after the Greek aphorism Panta Rhei (everything flows),
  provides functions to create publication-quality diagrams, using data in tables (or spread sheets)
  and a simple syntax.
	"""
	
	cran = "PantaRhei" 

	version("0.1.2", md5="ce368b2e37734302a6da682c1ae27161")

	depends_on("r@3.5:", type=("build", "run"))
