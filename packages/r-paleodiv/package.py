# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaleodiv(RPackage):
	"""Extracting and Visualizing Paleobiodiversity

	Contains various tools for conveniently downloading and editing taxon-specific datasets from the Paleobiology Database <https://paleobiodb.org>, extracting information on abundance, temporal distribution of subtaxa and taxonomic diversity through deep time, and visualizing these data in relation to phylogeny and stratigraphy.
	"""
	
	cran = "paleoDiv" 

	version("0.2.2", md5="f2a4fcb9b4005f2a783d7ffb4be31380")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
