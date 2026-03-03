# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHddesign(RPackage):
	"""Sample Size Calculation for High Dimensional Classification
Study

	Determine the sample size requirement to achieve the target probability of correct classification (PCC) for studies employing high-dimensional features.  The package implements functions to 1) determine the asymptotic feasibility of the classification problem; 2) compute the upper bounds of the PCC for any linear classifier; 3) estimate the PCC of three design methods given design assumptions; 4) determine the sample size requirement to achieve the target PCC for three design methods. 
	"""
	
	cran = "HDDesign" 

	version("1.1", md5="7d7ae91154a06569dd4d4a2202ec0217")

