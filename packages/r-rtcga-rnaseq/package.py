# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaRnaseq(RPackage):
	"""Rna-seq datasets from The Cancer Genome Atlas Project

	Package provides rna-seq datasets from The Cancer Genome Atlas Project for all cohorts types from http://gdac.broadinstitute.org/. Rna-seq data format is explained here https://wiki.nci.nih.gov/display/TCGA/RNASeq+Version+2. Data source is illumina hiseq Level 3 RSEM normalized expression data. Data from 2015-11-01 snapshot.
	"""
	
	bioc = "RTCGA.rnaseq" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/RTCGA.rnaseq_20151101.32.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/RTCGA.rnaseq/RTCGA.rnaseq_20151101.32.0.tar.gz"]

	version("20151101.32.0", md5="47bee14c68ff4d1014677eca0ed969a9")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rtcga", type=("build", "run"))

	# experiment