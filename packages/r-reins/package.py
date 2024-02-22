# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReins(RPackage):
	"""Functions from "Reinsurance: Actuarial and Statistical Aspects"

	Functions from the book "Reinsurance: Actuarial and Statistical Aspects" (2017) by Hansjoerg Albrecher, Jan Beirlant and Jef Teugels <https://www.wiley.com/en-us/Reinsurance%3A+Actuarial+and+Statistical+Aspects-p-9780470772683>.
	"""
	
	homepage = "https://github.com/TReynkens/ReIns"
	cran = "ReIns" 

	version("1.0.14", md5="52ad856a6ffc92a19a4df1fd2db06a7c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-foreach@1.4.1:", type=("build", "run"))
	depends_on("r-doparallel@1.0.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
