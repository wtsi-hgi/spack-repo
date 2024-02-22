# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvn(RPackage):
	"""Statistically Validated Networks

	Determines networks of significant synchronization between the discrete states of nodes; see Tumminello et al <doi:10.1371/journal.pone.0017994>.
	"""
	
	cran = "SVN" 

	version("1.0.1", md5="374745bc0dab8bfb8c021a15d3c606ae")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
