# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStreamdag(RPackage):
	"""Analytical Methods for Stream DAGs

	Provides indices and tools for directed acyclic graphs (DAGs), particularly DAG representations of intermittent streams.  A detailed introduction to the package can be found in the publication: "Non-perennial stream networks as directed acyclic graphs: The R-package streamDAG" (Aho et al., 2023) <doi:10.1016/j.envsoft.2023.105775>, and in the introductory package vignette.
	"""
	
	cran = "streamDAG" 

	version("1.5", md5="60c2280de35fb9c5feba9513eb96d198")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-asbio", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
