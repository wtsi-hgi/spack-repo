# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRise(RPackage):
	"""Conduct RISE Analysis

	Implements techniques for educational resource inspection, selection, and evaluation (RISE) described in Bodily, Nyland, and Wiley (2017) 
    <doi:10.19173/irrodl.v18i2.2952>.	Automates the process of identifying learning materials that are not effectively supporting student learning in 
    technology-mediated courses by synthesizing information about access to course content and performance on assessments.
	"""
	
	cran = "rise" 

	version("1.0.4", md5="c6a2b9d0d38201e1e51d8c0f9b805167")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
