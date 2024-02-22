# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdlei(RPackage):
	"""Cause-Deleted Life Expectancy Improvement Procedure

	The concept of cause-deleted life expectancy improvement is statistic designed to quantify the increase in life expectancy if a certain cause of death is removed. See Adamic, P. (2015) (<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2689352>).
	"""
	
	cran = "cdlei" 

	version("1.0", md5="52cacf7207e11e578b1c93515a7408ce")

	depends_on("r@3.5:", type=("build", "run"))
