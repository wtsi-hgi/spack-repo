# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTssRestrend(RPackage):
	"""Time Series Segmentation of Residual Trends

	Time Series Segmented Residual Trends is a method for the automated detection of land degradation from remotely sensed vegetation and climate datasets. TSS-RESTREND incorporates aspects of two existing degradation detection methods: RESTREND which is used to control for climate variability, and BFAST which is used to look for structural changes in the ecosystem. The full details of the testing and justification of the TSS-RESTREND method (version 0.1.02) are published in Burrell et al., (2017). <doi:10.1016/j.rse.2017.05.018>. The changes to the method introduced in version 0.2.03 focus on the inclusion  of temperature as an additional climate variable. This allows for land  degradation assessment in temperature limited drylands. A paper that details this work is currently under review. There are also a number of bug fixes and speed improvements. Version 0.3.0 introduces additional attribution for eCO2,  climate change and climate variability the details of which are in press in Burrell et al., (2020).  The version under active development and additional example scripts showing  how the package can be applied can be found at <https://github.com/ArdenB/TSSRESTREND>. 
	"""
	
	cran = "TSS.RESTREND" 

	version("0.3.1", md5="e0033bb413c4bc7119d08fb903840af0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bfast@1.5.7:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-mblm", type=("build", "run"))
