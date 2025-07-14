# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaMethylation(RPackage):
	"""Methylation datasets from The Cancer Genome Atlas Project

	Package provides methylation (humanmethylation27) datasets from The Cancer Genome Atlas Project for all available cohorts types from http://gdac.broadinstitute.org/. Data format is explained here https://wiki.nci.nih.gov/display/TCGA/DNA+methylation Data from 2015-11-01 snapshot.
	"""
	
	bioc = "RTCGA.methylation"

	version("1.36.0", commit="5fa177aaca1268b5017ae6d4b818970a35a63ae2")
	version("1.30.0", commit="af4156677b72d68ca3892db8e9801245ca7314e2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rtcga", type=("build", "run"))

