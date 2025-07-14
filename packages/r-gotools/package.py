# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGotools(RPackage):
	"""Functions for Gene Ontology database

	Wraper functions for description/comparison of oligo ID list using Gene Ontology database
	"""
	
	bioc = "goTools"

	version("1.82.0", commit="7c93e7d83c0b44ccdfb933d365b8212c9b1e1b24")
	version("1.76.0", commit="d860fb70826460519254e0987ad6d34b894bd8f6")

	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
