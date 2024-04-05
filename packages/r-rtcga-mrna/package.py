# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaMrna(RPackage):
	"""mRNA datasets from The Cancer Genome Atlas Project

	Package provides mRNA datasets from The Cancer Genome Atlas Project for all available cohorts types from http://gdac.broadinstitute.org/. Data format is explained here https://wiki.nci.nih.gov/display/TCGA/Gene+expression+data Data from 2015-11-01 snapshot.
	"""
	
	bioc = "RTCGA.mRNA" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RTCGA.mRNA_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RTCGA.mRNA/RTCGA.mRNA_1.30.0.tar.gz"]

	version("1.30.0", md5="c9774207df355ef5945677d36e915103")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rtcga", type=("build", "run"))

