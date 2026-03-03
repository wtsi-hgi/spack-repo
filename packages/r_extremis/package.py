# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtremis(RPackage):
	"""Statistics of Extremes

	Conducts inference in statistical models for extreme values (de Carvalho et al (2012), <doi:10.1080/03610926.2012.709905>; de Carvalho and Davison (2014), <doi:10.1080/01621459.2013.872651>; Einmahl et al (2016), <doi:10.1111/rssb.12099>).
	"""
	
	cran = "extremis" 

	version("1.2.1", md5="415220ae20ef96479c2e20370497710d")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-emplik", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
