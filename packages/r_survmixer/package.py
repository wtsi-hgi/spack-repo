# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvmixer(RPackage):
	"""Design of Clinical Trials with Survival Endpoints Based on
Binary Responses

	Sample size and effect size calculations for survival endpoints based on mixture survival-by-response model. The methods implemented can be found in  Bofill, Shen & Gómez (2021) <arXiv:2008.12887>. 
	"""
	
	cran = "survmixer" 

	version("1.3", md5="7110db2125c50112f51c897aa2c3a1a6")

