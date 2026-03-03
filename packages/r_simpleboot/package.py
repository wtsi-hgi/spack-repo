# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimpleboot(RPackage):
	"""Simple Bootstrap Routines

	Simple bootstrap routines.
	"""
	
	homepage = "https://github.com/rdpeng/simpleboot"
	cran = "simpleboot" 

	version("1.1-7", md5="d6b4e61164341f8ae953840353695805")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
