# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTenxvisiumdata(RPackage):
	"""Visium spatial gene expression data by 10X Genomics

	Collection of Visium spatial gene expression datasets by 10X Genomics, formatted into objects of class SpatialExperiment. Data cover various organisms and tissues, and include: single- and multi-section experiments, as well as single sections subjected to both whole transcriptome and targeted panel analysis. Datasets may be used for testing of and as examples in packages, for tutorials and workflow demonstrations, or similar purposes.
	"""
	
	homepage = "https://github.com/helenalc/TENxVisiumData"
	bioc = "TENxVisiumData"

	version("1.16.0", commit="e01f84e4a8179e086a537573316830f480d6cc7e")
	version("1.10.0", commit="6b160c1cd37b539724a70821d57617a14a8afd97")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))

