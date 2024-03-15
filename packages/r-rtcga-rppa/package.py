# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaRppa(RPackage):
	"""RPPA datasets from The Cancer Genome Atlas Project

	Package provides RPPA datasets from The Cancer Genome Atlas Project for all available cohorts types from http://gdac.broadinstitute.org/. Data format is explained here https://wiki.nci.nih.gov/display/TCGA/Protein+Array +Data+Format+Specification?src=search
	"""
	
	bioc = "RTCGA.RPPA" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RTCGA.RPPA_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RTCGA.RPPA/RTCGA.RPPA_1.30.0.tar.gz"]

	version("1.30.0", md5="5eccece412039d43cdf74aec284fa0d9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rtcga", type=("build", "run"))

	# experiment