# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNovelqualcodes(RPackage):
	"""Visualise the Path to a Stopping Point in Qualitative Interviews
Based on Novel Codes

	In semi-structured interviews that use the 'framework' method, it
    is not always clear how refinements to interview questions affect the
    decision of when to stop interviews. The trend of 'novel' and 'duplicate'
    interview codes (novel codes are information that other interviewees have
    not previously mentioned) provides insight into the richness of qualitative
    information. This package provides tools to visualise when refinements occur
    and how that affects the trends of novel and duplicate codes. These
    visualisations, when used progressively as new interviews are finished, can
    help the researcher to decide on a stopping point for their interviews.
	"""
	
	homepage = "https://github.com/DesiQuintans/novelqualcodes"
	cran = "novelqualcodes" 

	version("0.13.1", md5="bd42365251251eaefd32bea824f95f53")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-naturalsort", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpattern", type=("build", "run"))
