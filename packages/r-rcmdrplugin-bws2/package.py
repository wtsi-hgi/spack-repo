# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginBws2(RPackage):
	"""R Commander Plug-in for Case 2 Best-Worst Scaling

	Adds menu items for Case 2 (profile case) best-worst scaling (BWS2) to the R Commander. BWS2 is a question-based survey method that constructs profiles (combinations of attribute levels) using an orthogonal array, asks respondents to select the best and worst levels in each profile, and measures preferences for attribute levels by analyzing the responses. For details, see Aizaki and Fogarty (2019) <doi:10.1016/j.jocm.2019.100171>.
	"""
	
	cran = "RcmdrPlugin.BWS2" 

	version("0.2-0", md5="61a741fc255c653caadba92e6a6bd05c", url="https://cran.r-project.org/src/contrib/RcmdrPlugin.BWS2_0.2-0.tar.gz")

	depends_on("r-support-bws2@0.4.0:", type=("build", "run"))
	depends_on("r-support-ces", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcmdr", type=("build", "run"))
	depends_on("r-doe-base", type=("build", "run"))
