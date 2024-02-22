# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTempr(RPackage):
	"""Temporal Sensory Data Analysis

	Analysis and visualization of data from temporal sensory methods, including for temporal check-all-that-apply (TCATA) and temporal dominance of sensations (TDS). Methods are mainly from manuscripts by Castura, J.C., Antúnez, L., Giménez, A., and Ares, G. (2016) <doi:10.1016/j.foodqual.2015.06.017>, Castura, Baker, and Ross (2016) <doi:10.1016/j.foodqual.2016.06.011>, and Pineau et al. (2009) <doi:10.1016/j.foodqual.2009.04.005>.
	"""
	
	cran = "tempR" 

	version("0.9.9.23", md5="821218d1c392f778713bb7f1efe1cdd4")

	depends_on("r@4.1:", type=("build", "run"))
