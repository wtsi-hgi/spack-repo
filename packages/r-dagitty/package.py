# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDagitty(RPackage):
	"""Graphical Analysis of Structural Causal Models

	A port of the web-based software 'DAGitty', available at 
    <https://dagitty.net>, for analyzing structural causal models 
    (also known as directed acyclic graphs or DAGs).
    This package computes covariate adjustment sets for estimating causal
    effects, enumerates instrumental variables, derives testable
    implications (d-separation and vanishing tetrads), generates equivalent
    models, and includes a simple facility for data simulation. 
	"""
	
	homepage = "https://www.dagitty.net"
	cran = "dagitty" 

	version("0.3-4", md5="52bd65009157ddfe6d496bc79897c52f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
