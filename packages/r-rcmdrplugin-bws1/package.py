# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginBws1(RPackage):
	"""R Commander Plug-in for Case 1 Best-Worst Scaling

	Adds menu items to the R Commander for implementing case 1 (object case) best-worst scaling (BWS1) from designing choice sets to measuring preferences for items. BWS1 is a question-based survey method that constructs various combinations of items (choice sets) using the experimental designs, asks respondents to select the best and worst items in each choice set, and then measures preferences for the items by analyzing the responses. For details on BWS1, refer to Louviere et al. (2015) <doi:10.1017/CBO9781107337855>.
	"""
	
	cran = "RcmdrPlugin.BWS1" 

	version("0.2-1", md5="0c72b0dfb14a017a1ebed4d9aba0ca55", url="https://cran.r-project.org/src/contrib/RcmdrPlugin.BWS1_0.2-1.tar.gz")

	depends_on("r-crossdes", type=("build", "run"))
	depends_on("r-support-bws@0.4.1:", type=("build", "run"))
	depends_on("r-support-ces", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcmdr", type=("build", "run"))
