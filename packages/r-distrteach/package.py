# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistrteach(RPackage):
	"""Extensions of Package 'distr' for Teaching
Stochastics/Statistics in Secondary School

	Provides flexible examples of LLN and CLT for teaching purposes in secondary
            school.
	"""
	
	homepage = "http://distr.r-forge.r-project.org/"
	cran = "distrTeach" 

	version("2.9.1", md5="30e83904daa0ce814fc153be3f87447b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-distr@2.2:", type=("build", "run"))
	depends_on("r-distrex@2.2:", type=("build", "run"))
	depends_on("r-startupmsg", type=("build", "run"))
