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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RTCGA.methylation_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RTCGA.methylation/RTCGA.methylation_1.30.0.tar.gz"]

	version("1.30.0", sha256="3219d26bc1faec0d9394c88fb421ae41e53752cd879dae92f26f9472991ea4bc")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rtcga", type=("build", "run"))

