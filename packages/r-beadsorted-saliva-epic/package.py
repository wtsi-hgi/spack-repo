# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeadsortedSalivaEpic(RPackage):
	"""Illumina EPIC data on BeadSorted child saliva cells

	Raw data objects used to estimate saliva cell proportion estimates in ewastools. The FlowSorted.Saliva.EPIC object is constructed from samples assayed by Lauren Middleton et. al. (2021).
	"""
	
	bioc = "BeadSorted.Saliva.EPIC" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/BeadSorted.Saliva.EPIC_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/BeadSorted.Saliva.EPIC/BeadSorted.Saliva.EPIC_1.10.0.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="1cc58efe81f0599f691b35281c0433fec50f801f2da1ee51bf54b39367340c21")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-minfi@1.36:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

