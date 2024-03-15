# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginBws3(RPackage):
	"""R Commander Plug-in for Case 3 Best-Worst Scaling

	Adds menu items for case 3 (multi-profile) best-worst scaling (BWS3) to the R Commander. BWS3 is a question-based survey method that designs various combinations of attribute levels (profiles), asks respondents to select the best and worst profiles in each choice set, and then measures preferences for the attribute levels by analyzing the responses. For details on BWS3, refer to Louviere et al. (2015) <doi:10.1017/CBO9781107337855>.
	"""
	
	cran = "RcmdrPlugin.BWS3" 

	version("0.2-2", md5="c0aed847c3ec7ae2f6c59930833f070a", url="https://cran.r-project.org/src/contrib/RcmdrPlugin.BWS3_0.2-2.tar.gz")

	depends_on("r-support-bws3", type=("build", "run"))
	depends_on("r-support-ces", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcmdr", type=("build", "run"))
