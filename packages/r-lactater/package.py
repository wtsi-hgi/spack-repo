# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLactater(RPackage):
	"""Tools for Analyzing Lactate Thresholds

	Set of tools for analyzing lactate thresholds from a step incremental test to exhaustion. Easily analyze
    the methods Log-log, Onset of Blood Lactate Accumulation (OBLA), Baseline plus (Bsln+), Dmax, Lactate Turning Point (LTP),
    and Lactate / Intensity ratio (LTratio) in cycling, running, or swimming.
    Beaver WL, Wasserman K, Whipp BJ (1985) <doi:10.1152/jappl.1985.59.6.1936>.
    Heck H, Mader A, Hess G, Mücke S, Müller R, Hollmann W (1985) <doi:10.1055/s-2008-1025824>.
    Kindermann W, Simon G, Keul J (1979) <doi:10.1007/BF00421101>.
    Skinner JS, Mclellan TH (1980) <doi:10.1080/02701367.1980.10609285>.
    Berg A, Jakob E, Lehmann M, Dickhuth HH, Huber G, Keul J (1990) PMID 2408033.
    Zoladz JA, Rademaker AC, Sargeant AJ (1995) <doi:10.1113/jphysiol.1995.sp020959>.
    Cheng B, Kuipers H, Snyder A, Keizer H, Jeukendrup A, Hesselink M (1992) <doi:10.1055/s-2007-1021309>.
    Bishop D, Jenkins DG, Mackinnon LT (1998) <doi:10.1097/00005768-199808000-00014>.
    Hughson RL, Weisiger KH, Swanson GD (1987) <doi:10.1152/jappl.1987.62.5.1975>.
    Jamnick NA, Botella J, Pyne DB, Bishop DJ (2018) <doi:10.1371/journal.pone.0199794>.
    Hofmann P, Tschakert G (2017) <doi:10.3389/fphys.2017.00337>.
    Hofmann P, Pokan R, von Duvillard SP, Seibert FJ, Zweiker R, Schmid P (1997) <doi:10.1097/00005768-199706000-00005>.
    Pokan R, Hofmann P, Von Duvillard SP, et al. (1997) <doi:10.1097/00005768-199708000-00009>.
    Dickhuth H-H, Yin L, Niess A, et al. (1999) <doi:10.1055/s-2007-971105>.
	"""
	
	cran = "lactater" 

	version("0.2.0", md5="7fc0df2917b1efbfb2f8b68827bec489")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
