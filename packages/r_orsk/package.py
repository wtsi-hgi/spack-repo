# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrsk(RPackage):
	"""Converting Odds Ratio to Relative Risk in Cohort Studies with
Partial Data Information

	Convert odds ratio to relative risk in cohort studies with partial data information (Wang (2013) <doi:10.18637/jss.v055.i05>).
	"""
	
	cran = "orsk" 

	version("1.0-8", md5="f25679280746e3c8145ca2ab811cb051")

	depends_on("r-bb", type=("build", "run"))
	depends_on("r-bhh2", type=("build", "run"))
