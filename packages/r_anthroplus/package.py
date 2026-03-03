# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnthroplus(RPackage):
	"""Computation of the WHO 2007 References for School-Age Children
and Adolescents (5 to 19 Years)

	Provides WHO 2007 References for School-age Children and
             Adolescents (5 to 19 years) (z-scores) with
             confidence intervals and standard errors around the
             prevalence estimates, taking into account complex sample designs.
             More information on the methods is
             available online:
             <https://www.who.int/tools/growth-reference-data-for-5to19-years>.
	"""
	
	cran = "anthroplus" 

	version("0.9.0", md5="e9058157a4af501b677ab8fc59942835")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-anthro@1:", type=("build", "run"))
