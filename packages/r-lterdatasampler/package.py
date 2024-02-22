# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLterdatasampler(RPackage):
	"""Educational Dataset Examples from the Long Term Ecological
Research Program

	Curated datasets from US Long Term Ecological Research sites. 
	"""
	
	homepage = "https://github.com/lter/lterdatasampler"
	cran = "lterdatasampler" 

	version("0.1.1", md5="11ad6af422fa255befe2258530cce3a3")

	depends_on("r@2.10:", type=("build", "run"))
