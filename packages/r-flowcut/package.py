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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/flowCut_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/flowCut/flowCut_1.12.0.tar.gz"]

	version("1.12.0", md5="b79bc38dd887cef19040c2d7178311d0")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowdensity@1.13.1:", type=("build", "run"))
	depends_on("r-cairo", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
