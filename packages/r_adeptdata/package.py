# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdeptdata(RPackage):
	"""Accelerometry Data Sets

	Created to host raw accelerometry data sets and their derivatives which are used in the corresponding 'adept' package.
	"""
	
	cran = "adeptdata" 

	version("1.1", md5="87383514bd436cbcbdf752d794eac99a")

	depends_on("r@2.10:", type=("build", "run"))
