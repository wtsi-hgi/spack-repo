# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCormotif(RPackage):
	"""Correlation Motif Fit

	It fits correlation motif model to multiple studies to detect study specific differential expression patterns.
	"""
	
	bioc = "Cormotif"

	version("1.54.0", commit="0fc2c06e10f4a70af16b176504f0022f8ebcbc11")
	version("1.48.0", commit="ed355f194acd6f7b2a2344834a0b21bc757a1e36")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
