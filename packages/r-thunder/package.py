# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThunder(RPackage):
	"""Computation and Visualisation of Atmospheric Convective
Parameters

	Allow to compute and visualise convective parameters commonly
  used in the operational prediction of severe convective storms. Core algorithm
  is based on a highly optimized 'C++' code linked into 'R' via 'Rcpp'. Highly
  efficient engine allows to derive thermodynamic and kinematic parameters from
  large numerical datasets such as reanalyses or operational Numerical Weather 
  Prediction models in a reasonable amount of time. Package has been developed
  since 2017 by research meteorologists specializing in severe thunderstorms.
  The most relevant methods used in the package based on the following publications
  Stipanuk (1973) <https://apps.dtic.mil/sti/pdfs/AD0769739.pdf>,
  McCann et al. (1994) <doi:10.1175/1520-0434(1994)009%3C0532:WNIFFM%3E2.0.CO;2>,
  Bunkers et al. (2000) <doi:10.1175/1520-0434(2000)015%3C0061:PSMUAN%3E2.0.CO;2>,
  Corfidi et al. (2003) <doi:10.1175/1520-0434(2003)018%3C0997:CPAMPF%3E2.0.CO;2>,
  Showalter (1953) <doi:10.1175/1520-0477-34.6.250>,
  Coffer et al. (2019) <doi:10.1175/WAF-D-19-0115.1>,
  Gropp and Davenport (2019) <doi:10.1175/WAF-D-17-0150.1>,
  Czernecki et al. (2019) <doi:10.1016/j.atmosres.2019.05.010>,
  Taszarek et al. (2020) <doi:10.1175/JCLI-D-20-0346.1>,
  Sherburn and Parker (2014) <doi:10.1175/WAF-D-13-00041.1>,
  Romanic et al. (2022) <doi:10.1016/j.wace.2022.100474>.
	"""
	
	homepage = "https://bczernecki.github.io/thundeR/"
	cran = "thunder" 

	version("1.1.3", md5="2435ad3386eb2fd38a53c863ad8b8d0b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-airthermo", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
