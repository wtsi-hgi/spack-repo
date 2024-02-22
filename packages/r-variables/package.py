# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVariables(RPackage):
	"""Variable Descriptions

	Abstract descriptions of (yet) unobserved variables.
	"""
	
	homepage = "http://ctm.R-forge.R-project.org"
	cran = "variables" 

	version("1.1-1", md5="224c2206b1d4d1baeb2862618068e89a")

