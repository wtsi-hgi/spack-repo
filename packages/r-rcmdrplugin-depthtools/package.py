# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginDepthtools(RPackage):
	"""R Commander Depth Tools Plug-in

	We provide an Rcmdr plug-in based on the depthTools 
        package, which implements different robust statistical tools 
        for the description and analysis of gene expression data based 
        on the Modified Band Depth, namely, the scale curves for 
        visualizing the dispersion of one or various groups of samples
        (e.g. types of tumors), a rank test to decide whether two
        groups of samples come from a single distribution and two 
        methods of supervised classification techniques, the DS and 
        TAD methods.
	"""
	
	cran = "RcmdrPlugin.depthTools" 

	version("1.4", md5="a6882b69874b294a76629d9d36a328d3")

	depends_on("r-rcmdr@1.4.0:", type=("build", "run"))
	depends_on("r-depthtools", type=("build", "run"))
