# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaCnv(RPackage):
	"""CNV (Copy-number variation) datasets from The Cancer Genome Atlas Project

	Package provides CNV (based on Merge snp) datasets from The Cancer Genome Atlas Project for all cohorts types from http://gdac.broadinstitute.org/. Data format is explained here https://wiki.nci.nih.gov/display/TCGA/Retrieving +Data+Using+the+Data+Matrix. Data from 2015-11-01 snapshot.
	"""
	
	bioc = "RTCGA.CNV" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RTCGA.CNV_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RTCGA.CNV/RTCGA.CNV_1.30.0.tar.gz"]

	version("1.30.0", md5="15267c2322da59ccd344657a28d2ba6a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rtcga", type=("build", "run"))

