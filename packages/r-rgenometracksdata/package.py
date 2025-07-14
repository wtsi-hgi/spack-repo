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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rGenomeTracksData_0.99.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rGenomeTracksData/rGenomeTracksData_0.99.0.tar.gz"]

	version("0.99.0", tag="RELEASE_3_21")
	version("0.99.0", sha256="6a0a73f0a24c8ae370d8e0ce8d564148d16072fea7c23f75b666819500412fad")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

