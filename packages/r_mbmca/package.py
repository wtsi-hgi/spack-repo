# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbmca(RPackage):
	"""Nucleic Acid Melting Curve Analysis

	Lightweight utilities for nucleic acid melting curve analysis are 
    important in life sciences and diagnostics. This software can be used for 
    the analysis and presentation of melting curve data from microbead-based 
    assays (surface melting curve analysis) and reactions in solution (e.g., 
    quantitative PCR (qPCR), real-time isothermal Amplification). Further 
    information are described in detail in two publications in The R Journal [
    <https://journal.r-project.org/archive/2013-2/roediger-bohm-schimke.pdf>; 
    <https://journal.r-project.org/archive/2015-1/RJ-2015-1.pdf>].
	"""
	
	homepage = "https://github.com/PCRuniversum/MBmca/"
	cran = "MBmca" 

	version("1.0.1-3", md5="5d5c04ea0549e5e06b2526c8fa106930")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-robustbase@0.9:", type=("build", "run"))
	depends_on("r-chippcr@0.0.7:", type=("build", "run"))
