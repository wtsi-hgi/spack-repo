# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginDce(RPackage):
	"""R Commander Plug-in for Discrete Choice Experiments

	Adds menu items for discrete choice experiments (DCEs) to the R Commander. DCE is a question-based survey method that designs various combinations (profiles) of attribute levels using the experimental designs, asks respondents to select the most preferred profile in each choice set, and then measures preferences for the attribute levels by analyzing the responses. For details on DCEs, refer to Louviere et al. (2000) <doi:10.1017/CBO9780511753831>.
	"""
	
	cran = "RcmdrPlugin.DCE" 

	version("0.2-1", md5="a96a0b46c8d2eda1567f7d0c89222f72")

	depends_on("r-support-ces@0.7.0:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcmdr", type=("build", "run"))
