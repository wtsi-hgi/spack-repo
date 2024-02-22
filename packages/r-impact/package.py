# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImpact(RPackage):
	"""The Impact of Items

	Implement a multivariate analysis of the impact of items to identify a bias in the questionnaire validation of Likert-type scale variables. The items requires considering a null value (category doesn't have tendency). Offering frequency, importance and impact of the items.
	"""
	
	homepage = "http://www.uv.mx/personal/nehuerta/impact"
	cran = "IMPACT" 

	version("0.1.1", md5="e9cc052c21bc38fe196411971ca17328")

	depends_on("r@3:", type=("build", "run"))
