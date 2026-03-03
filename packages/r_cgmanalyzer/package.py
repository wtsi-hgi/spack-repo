# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCgmanalyzer(RPackage):
	"""Continuous Glucose Monitoring Data Analyzer

	Contains all of the functions necessary for the complete analysis of a continuous glucose monitoring study and can be applied to data measured by various existing 'CGM' devices such as 'FreeStyle Libre', 'Glutalor', 'Dexcom' and 'Medtronic CGM'. It reads a series of data files, is able to convert various formats of time stamps, can deal with missing values, calculates both regular statistics and nonlinear statistics, and conducts group comparison. It also displays results in a concise format. Also contains two unique features new to 'CGM' analysis: one is the implementation of strictly standard mean difference and the class of effect size; the other is the development of a new type of plot called antenna plot. It corresponds to 'Zhang XD'(2018)<doi:10.1093/bioinformatics/btx826>'s article 'CGManalyzer: an R package for analyzing continuous glucose monitoring studies'.
	"""
	
	cran = "CGManalyzer" 

	version("1.3.1", md5="8538567422a3347e1d18160a7d09bf22")

