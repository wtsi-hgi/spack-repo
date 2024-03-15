# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrmeta(RPackage):
	"""Correlated Meta-Analysis

	Performs Correlated Meta-Analysis ('corrmeta') across multiple OMIC
        scans, accounting for hidden non-independencies between elements of the
        scans due to overlapping samples, related samples, or other information. 
        For more information about the method, refer to the paper
        Province MA. (2013) <doi:10.1142/9789814447973_0023>.
	"""
	
	cran = "corrmeta" 

	version("1.0.0", md5="2f91a94e3880734c87353bf9db2ae1c9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
