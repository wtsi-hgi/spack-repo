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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RTCGA.miRNASeq_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RTCGA.miRNASeq/RTCGA.miRNASeq_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="64ec211586dd6077f2d6a5e24bd9781643adf22e2d667c17f6706d42d8396bc3")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rtcga", type=("build", "run"))

