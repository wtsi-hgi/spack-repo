# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetseg(RPackage):
	"""Measures of Network Segregation and Homophily

	Segregation is a network-level property such that edges between 
  predefined groups of vertices are relatively less likely. Network homophily 
  is a individual-level tendency to form relations with people who are similar 
  on some attribute (e.g. gender, music taste, social status, etc.). In general
  homophily leads to segregation, but segregation might arise without 
  homophily. This package implements descriptive indices measuring 
  homophily/segregation. It is a computational companion 
  to Bojanowski & Corten (2014) <doi:10.1016/j.socnet.2014.04.001>.
	"""
	
	homepage = "https://mbojan.github.io/netseg/"
	cran = "netseg" 

	version("1.0-2", md5="31016d2cc1337b34a3e321c786b92824")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph@0.6.0:", type=("build", "run"))
