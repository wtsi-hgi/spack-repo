# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtaxg(RPackage):
	"""Diagnostic Test Assessment in the Absence of Gold Standard

	To calculate the sensitivity and specificity in the absence of gold standard using the Bayesian method.
    The Bayesian method can be referenced at Haiyan Gu and Qiguang Chen (1999) <doi:10.3969/j.issn.1002-3674.1999.04.004>.
	"""
	
	cran = "DTAXG" 

	version("0.1.0", md5="3b63050e0b1177141b6e5c0b0cb5dd63")

