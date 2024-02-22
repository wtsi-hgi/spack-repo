# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtlnet(RPackage):
	"""Causal Inference of QTL Networks

	Functions to Simultaneously Infer Causal Graphs and Genetic Architecture.
  Includes acyclic and cyclic graphs for data from an experimental cross with a modest number (<10) of phenotypes driven by
  a few genetic loci (QTL).
  Chaibub Neto E, Keller MP, Attie AD, Yandell BS (2010)
  Causal Graphical Models in Systems Genetics: a unified framework for joint inference of causal network and genetic architecture for correlated phenotypes.
  Annals of Applied Statistics 4: 320-339.
  <doi:10.1214/09-AOAS288>.
	"""
	
	homepage = "http://www.stat.wisc.edu/~yandell/sysgen"
	cran = "qtlnet" 

	version("1.5.4", md5="71ef371dd60c52cfd06cf2323afdc6cd")

	depends_on("r-qtl", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sem", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-pcalg", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
