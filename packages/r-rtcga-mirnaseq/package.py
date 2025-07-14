# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaMirnaseq(RPackage):
	"""miRNASeq datasets from The Cancer Genome Atlas Project

	Package provides miRNASeq datasets from The Cancer Genome Atlas Project for all available cohorts types from http://gdac.broadinstitute.org/. Data format is explained here https://wiki.nci.nih.gov/display/TCGA/miRNASeq#miRNASeq-DataOverview Data from 2015-11-01 snapshot.
	"""
	
	bioc = "RTCGA.miRNASeq"

	version("1.36.0", commit="d189b24e0db55443eec04e96de5a616644b34c0c")
	version("1.30.0", commit="188959b9ca0b02a6ed340d04c8bce90eb1c94f37")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rtcga", type=("build", "run"))

