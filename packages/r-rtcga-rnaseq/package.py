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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RTCGA.rnaseq_20151101.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RTCGA.rnaseq/RTCGA.rnaseq_20151101.32.0.tar.gz"]

    version("20151101.38.0", tag="RELEASE_3_21")
	version("20151101.32.0", sha256="4c4ff26f6039065c4a6195f6a3fda316e91a3647967233caf9ba4d73714bb6da")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rtcga", type=("build", "run"))

