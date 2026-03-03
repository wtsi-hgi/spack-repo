# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcs(RPackage):
	"""Model Confidence Set Procedure

	Perform the model confidence set procedure of Hansen et al (2011) <doi:10.3982/ECTA5771>.
	"""
	
	cran = "MCS" 

	version("0.1.3", md5="d0c69473734075af0dabab2fedfb3f5b")

	depends_on("r@3.0.1:", type=("build", "run"))
