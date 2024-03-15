# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContingencytables(RPackage):
	"""Statistical Analysis of Contingency Tables

	Provides functions to perform statistical inference of data organized in contingency tables. This package is a companion to the "Statistical Analysis of Contingency Tables" book by Fagerland et al. <ISBN 9781466588172>.
	"""
	
	homepage = "https://contingencytables.com/"
	cran = "contingencytables" 

	version("3.0.0", md5="f0298394338ff1ac005ecf8f2c783717")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
