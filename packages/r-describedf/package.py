# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDescribedf(RPackage):
	"""Description of a Data Frame

	Helps to describe a data frame in hand. Has been developed during PhD work of the maintainer. More information may be obtained from Garai and Paul (2023) <doi:10.1016/j.iswa.2023.200202>.
	"""
	
	cran = "DescribeDF" 

	version("0.2.1", md5="50539a7cf43b60f2a752190f0fbe3239")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-fnonlinear", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
