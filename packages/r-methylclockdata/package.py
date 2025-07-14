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

	version("1.16.0", commit="d7ae1e2ec9510d22163e56b5abe7dcdb7e4b5be6")
	version("1.10.0", commit="276ec3cf5ca25929383623d5432f2ae200ffcc16")

	depends_on("r-experimenthubdata", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

