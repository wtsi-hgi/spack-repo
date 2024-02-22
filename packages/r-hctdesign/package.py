# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHctdesign(RPackage):
	"""Group Sequential Design for Historical Control Trial with
Survival Outcome

	It provides functions to design historical controlled trials with survival outcome by group sequential method. The options for interim look boundaries are efficacy only, efficacy & futility or futility only. It also provides the function to monitor the trial for any unplanned look. The package is based on Jianrong Wu, Xiaoping Xiong (2016) <doi:10.1002/pst.1756> and Jianrong Wu, Yimei Li (2020) <doi:10.1080/10543406.2019.1684305>.
	"""
	
	cran = "HCTDesign" 

	version("0.7.2", md5="828424a503ff33cb01d13087754fa996")

	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-diversitree", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
