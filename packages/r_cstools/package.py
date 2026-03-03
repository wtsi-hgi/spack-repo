# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCstools(RPackage):
	"""Assessing Skill of Climate Forecasts on Seasonal-to-Decadal
Timescales

	Exploits dynamical seasonal forecasts in order to provide
    information relevant to stakeholders at the seasonal timescale. The package
    contains process-based methods for forecast calibration, bias correction,
    statistical and stochastic downscaling, optimal forecast combination and
    multivariate verification, as well as basic and advanced tools to obtain
    tailored products. This package was developed in the context of the 'ERA4CS' 
    project 'MEDSCOPE' and the 'H2020 S2S4E' project and includes contributions from 
    'ArticXchange' project founded by 'EU-PolarNet 2'.
    'Pérez-Zanón et al. (2022) <doi:10.5194/gmd-15-6115-2022>'.
    'Doblas-Reyes et al. (2005) <doi:10.1111/j.1600-0870.2005.00104.x>'.
    'Mishra et al. (2018) <doi:10.1007/s00382-018-4404-z>'.
    'Sanchez-Garcia et al. (2019) <doi:10.5194/asr-16-165-2019>'.
    'Straus et al. (2007) <doi:10.1175/JCLI4070.1>'.
    'Terzago et al. (2018) <doi:10.5194/nhess-18-2825-2018>'.
    'Torralba et al. (2017) <doi:10.1175/JAMC-D-16-0204.1>'.
    'D'Onofrio et al. (2014) <doi:10.1175/JHM-D-13-096.1>'.
    'Verfaillie et al. (2017) <doi:10.5194/gmd-10-4257-2017>'.
    'Van Schaeybroeck et al. (2019) <doi:10.1016/B978-0-12-812372-0.00010-8>'.
    'Yiou et al. (2013) <doi:10.1007/s00382-012-1626-3>'.
	"""
	
	cran = "CSTools" 

	version("5.2.0", md5="262e73415a1971dd4b4d7a5b2ef894e9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-qmap", type=("build", "run"))
	depends_on("r-easyverification", type=("build", "run"))
	depends_on("r-s2dv", type=("build", "run"))
	depends_on("r-startr", type=("build", "run"))
	depends_on("r-rainfarmr", type=("build", "run"))
	depends_on("r-multiapply@2.1.1:", type=("build", "run"))
	depends_on("r-climprojdiags", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-verification", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-easyncdf", type=("build", "run"))
