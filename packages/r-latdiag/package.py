# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLatdiag(RPackage):
	"""Draws Diagrams Useful for Checking Latent Scales

	A graph
  proposed by Rosenbaum is useful
  for checking some properties of various
  sorts of latent scale, this program generates commands
  to obtain the graph using 'dot' from 'graphviz'.
	"""
	
	cran = "latdiag" 

	version("0.3", md5="1bdc379959a96b1f8bfd126c53589a24")

	depends_on("r-rdpack", type=("build", "run"))
	depends_on("graphviz", type=("build", "link", "run"))
