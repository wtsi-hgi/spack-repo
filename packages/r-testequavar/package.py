# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestequavar(RPackage):
	"""Bootstrap Tests for Equality of 2, 3, or 4 Population Variances

	Tests the hypothesis  that variances are homogeneous or not using bootstrap. The procedure uses a variance-based statistic, and is derived from a normal-theory test.
             The test equivalently expressed the hypothesis as a function of the log contrasts of the population variances. A box-type acceptance region is constructed to test the hypothesis. See Cahoy (2010) doi{10.1016/j.csda.2010.04.012}.
	"""
	
	cran = "testequavar" 

	version("0.1.5", md5="00d12ac4889a712be9a3205bfcfbf8cc")

