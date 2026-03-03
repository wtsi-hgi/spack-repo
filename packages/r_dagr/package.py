# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDagr(RPackage):
	"""Directed Acyclic Graphs: Analysis and Data Simulation

	Draw, manipulate, and evaluate directed
        acyclic graphs and simulate corresponding data, as described in International Journal of Epidemiology 50(6):1772-1777.
	"""
	
	cran = "dagR" 

	version("1.2.1", md5="98a61e358712377211177485d53bfd34")

