# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomnames(RPackage):
	"""Generate Random Given and Surnames

	Function for generating random gender and ethnicity correct first and/or last names. Names are chosen proportionally based upon their probability of appearing in a large scale data base of real names.
	"""
	
	homepage = "https://CenterForAssessment.github.io/randomNames"
	cran = "randomNames" 

	version("1.5-0.0", md5="ed8b848917af554bb85c49ec88555305")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-toordinal@1.1:", type=("build", "run"))
