# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRisk(RPackage):
	"""Computes 26 Financial Risk Measures for Any Continuous
Distribution

	Computes 26 financial risk measures for any continuous distribution.  The 26 financial risk measures  include value at risk, expected shortfall due to Artzner et al. (1999) <DOI:10.1007/s10957-011-9968-2>, tail conditional median due to Kou et al. (2013) <DOI:10.1287/moor.1120.0577>, expectiles due to Newey and Powell (1987) <DOI:10.2307/1911031>, beyond value at risk due to Longin (2001) <DOI:10.3905/jod.2001.319161>, expected proportional shortfall due to Belzunce et al. (2012) <DOI:10.1016/j.insmatheco.2012.05.003>, elementary risk measure due to Ahmadi-Javid (2012) <DOI:10.1007/s10957-011-9968-2>, omega due to Shadwick and Keating (2002), sortino ratio due to Rollinger and Hoffman (2013), kappa  due to Kaplan and Knowles  (2004), Wang (1998)'s <DOI:10.1080/10920277.1998.10595708> risk measures, Stone (1973)'s <DOI:10.2307/2978638> risk measures, Luce (1980)'s <DOI:10.1007/BF00135033> risk measures, Sarin (1987)'s <DOI:10.1007/BF00126387> risk measures, Bronshtein and Kurelenkova (2009)'s risk measures.
	"""
	
	cran = "Risk" 

	version("1.0", md5="57a81f8fbbd3e142e262e4ca82bcb5e0")

	depends_on("r@3.0.1:", type=("build", "run"))
