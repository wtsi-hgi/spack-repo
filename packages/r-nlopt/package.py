# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlopt(RPackage):
	"""Call Optimization Solvers with .nl Files

	The purpose of this library is to to call different optimization solvers (such as Gonzalez Rodriguez et al. (2022) <doi:10.1007/s10898-022-01229-w>, Tawarmalani and Sahinidis (2005) <doi:10.1007/s10107-005-0581-8>, and Byrd et al. (2006) <doi:10.1007/0-387-30065-1_4>) to solve problems given by a standard nl file.
	"""
	
	cran = "nlopt" 

	version("0.1.1", md5="c6b005a654389f871f6b76daa9bb0385")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("nlopt", type=("build", "link", "run"))
