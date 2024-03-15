# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaMutations(RPackage):
	"""Mutations datasets from The Cancer Genome Atlas Project

	Package provides mutations datasets from The Cancer Genome Atlas Project for all cohorts types from http://gdac.broadinstitute.org/. Mutations data format is explained here https://wiki.nci.nih.gov/display/TCGA/Mutation+Annotation+Format+(MAF)+Specification. There is extra one column with patients' barcodes. Data from 2015-11-01 snapshot.
	"""
	
	bioc = "RTCGA.mutations" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RTCGA.mutations_20151101.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RTCGA.mutations/RTCGA.mutations_20151101.32.0.tar.gz"]

	version("20151101.32.0", md5="0740acb5a6a47fd9d1281ccaf80bafed")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rtcga", type=("build", "run"))

	# experiment