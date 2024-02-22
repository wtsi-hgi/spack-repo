# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXrscc(RPackage):
	"""Statistical Quality Control Simulation

	This is a set of statistical quality control functions,  that allows plotting control charts and its iterations, process capability for variable and attribute control, highlighting the xrs_gr() function, like a first iteration for variable chart, meanwhile the we_rules() function detects non random patterns in sample.
	"""
	
	cran = "XRSCC" 

	version("0.1", md5="a27f1686faa69a424df20beb254f996f")

