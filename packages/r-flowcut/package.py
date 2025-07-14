# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowcut(RPackage):
	"""Automated Removal of Outlier Events and Flagging of Files Based on Time Versus Fluorescence Analysis

	Common techinical complications such as clogging can result in spurious events and fluorescence intensity shifting, flowCut is designed to detect and remove technical artifacts from your data by removing segments that show statistical differences from other segments.
	"""
	
	bioc = "flowCut"

	version("1.18.0", commit="3bc7f4953500925c158e8810834a7bed18c11368")
	version("1.12.0", commit="6c7d2a70c14174901ea7c589832fda4e838b306a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowdensity@1.13.1:", type=("build", "run"))
	depends_on("r-cairo", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
