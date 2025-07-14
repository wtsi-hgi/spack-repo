# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgenometracksdata(RPackage):
	"""Demonstration Data from rGenomeTracks Package

	rGenomeTracksData is a collection of data from pyGenomeTracks project. The purpose of this data is testing and demonstration of rGenomeTracks. This package include 14 sample file from different genomic and epigenomic file format.
	"""
	
	bioc = "rGenomeTracksData"

	version("0.99.0", commit="dc10aca5fc652ce359e8130ff8bb4398a15b9a2a")
	version("0.99.0", commit="dc10aca5fc652ce359e8130ff8bb4398a15b9a2a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

