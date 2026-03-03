# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmw(RPackage):
	"""Understanding Nonlinear Mixed Effects Modeling for Population
Pharmacokinetics

	This shows how NONMEM(R) software works. NONMEM's classical estimation methods like 'First Order(FO) approximation', 'First Order Conditional Estimation(FOCE)', and 'Laplacian approximation' are explained.
	"""
	
	homepage = "https://cran.r-project.org/package=nmw"
	cran = "nmw" 

	version("0.1.5", md5="dd3a1fc1601a076f4eac3f0ca7702316")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
