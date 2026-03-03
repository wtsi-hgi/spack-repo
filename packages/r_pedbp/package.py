# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedbp(RPackage):
	"""Pediatric Blood Pressure

	Data and utilities for estimating pediatric blood pressure
    percentiles by sex, age, and optionally height (stature) as described in
    Martin et.al. (2022) <doi:10.1001/jamanetworkopen.2022.36918>.
    Blood pressure percentiles for children under one year of age come from Gemelli
    et.al. (1990) <doi:10.1007/BF02171556>.  Estimates of blood pressure
    percentiles for children at least one year of age are informed by
    data from the National Heart, Lung, and Blood Institute (NHLBI) and the
    Centers for Disease Control and Prevention (CDC)
    <doi:10.1542/peds.2009-2107C> or from Lo et.al. (2013)
    <doi:10.1542/peds.2012-1292>.  The flowchart for selecting the informing
    data source comes from Martin et.al. (2022)
    <doi:10.1542/hpeds.2021-005998>.
	"""
	
	homepage = "https://github.com/dewittpe/pedbp/"
	cran = "pedbp" 

	version("1.0.2", md5="569f780257865ee2cadc35ee634c7540")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
