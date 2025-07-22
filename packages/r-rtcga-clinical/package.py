# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaClinical(RPackage):
	"""Clinical datasets from The Cancer Genome Atlas Project

	Package provides clinical datasets from The Cancer Genome Atlas Project for all cohorts types from http://gdac.broadinstitute.org/. Clinical data format is explained here https://wiki.nci.nih.gov/display/TCGA/Clinical+Data+Overview. Data from 2015-11-01 snapshot.
	"""
	
	bioc = "RTCGA.clinical" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RTCGA.clinical_20151101.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RTCGA.clinical/RTCGA.clinical_20151101.32.0.tar.gz"]

	version("20151101.38.0", tag="RELEASE_3_21")
	version("20151101.32.0", sha256="af8465683e165c17f45b253bf382e76cd57b7640c530b28f412a6d637ec26e47")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rtcga", type=("build", "run"))

