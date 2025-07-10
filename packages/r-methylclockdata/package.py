# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylclockdata(RPackage):
	"""Data for methylclock package

	Collection of 9 datasets, andrews and bakulski cord blood, blood gse35069, blood gse35069 chen, blood gse35069 complete, combined cord blood, cord bloo d gse68456, gervin and lyle cord blood, guintivano dlpfc and saliva gse48472". Data downloaded from [meffil](https://github.com/perishky/meffil/). Data used to estimate cell counts using Extrinsic epigenetic age acceleration (EEAA) method Collection of 12 datasets to use with MethylClock package to estimate chronological and gestational DNA methylationwith estimators to use wit different methylation clocks
	"""
	
	homepage = "https://github.com/isglobal-brge/methylclockData"
	bioc = "methylclockData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/methylclockData_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/methylclockData/methylclockData_1.10.0.tar.gz"]

	version("1.10.0", sha256="7eb08a0ea554c3e73a8bced5ba60a0f03d22809abcadcde700cf01cd298b9060")

	depends_on("r-experimenthubdata", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

