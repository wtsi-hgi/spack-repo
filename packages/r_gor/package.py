# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGor(RPackage):
	"""Algorithms for the Subject Graphs and Network Optimization

	Informal implementation of some algorithms from Graph
  Theory and Combinatorial Optimization which arise in the subject
  "Graphs and Network Optimization" from first course of the EUPLA
  (Escuela Universitaria Politecnica de La Almunia) degree of Data
  Engineering in Industrial Processes.
  References used are:
  Cook et al (1998, ISBN:0-471-55894-X),
  Korte, Vygen (2018) <doi:10.1007/978-3-662-56039-6>,
  Hromkovic (2004) <doi:10.1007/978-3-662-05269-3>,
  Hartmann, Weigt (2005, ISBN:978-3-527-40473-5).
	"""
	
	cran = "gor" 

	version("1.0", md5="13e8bc290b2a162535b7b35ee0a3e016")

	depends_on("r-igraph", type=("build", "run"))
