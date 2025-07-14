# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBodymaprat(RPackage):
	"""Experimental dataset from the rat BodyMap project

	This package contains a SummarizedExperiment from the Yu et al. (2013) paper that performed the rat BodyMap across 11 organs and 4 developmental stages. Raw FASTQ files were downloaded and mapped using STAR. Data is available on ExperimentHub as a data package.
	"""
	
	bioc = "bodymapRat"

	version("1.24.0", commit="ee1600b9f570b3f9e7df1d87a43558fc8cb13818")
	version("1.18.0", commit="af297a23988c6a3c795ff865d7389ed66974a012")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

