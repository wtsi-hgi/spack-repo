# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurveillance(RPackage):
	"""Temporal and Spatio-Temporal Modeling and Monitoring of Epidemic
Phenomena

	Statistical methods for the modeling and monitoring of time series
    of counts, proportions and categorical data, as well as for the modeling
    of continuous-time point processes of epidemic phenomena.
    The monitoring methods focus on aberration detection in count data time
    series from public health surveillance of communicable diseases, but
    applications could just as well originate from environmetrics,
    reliability engineering, econometrics, or social sciences. The package
    implements many typical outbreak detection procedures such as the
    (improved) Farrington algorithm, or the negative binomial GLR-CUSUM
    method of Hoehle and Paul (2008) <doi:10.1016/j.csda.2008.02.015>.
    A novel CUSUM approach combining logistic and multinomial logistic
    modeling is also included. The package contains several real-world data
    sets, the ability to simulate outbreak data, and to visualize the
    results of the monitoring in a temporal, spatial or spatio-temporal
    fashion. A recent overview of the available monitoring procedures is
    given by Salmon et al. (2016) <doi:10.18637/jss.v070.i10>.
    For the retrospective analysis of epidemic spread, the package provides
    three endemic-epidemic modeling frameworks with tools for visualization,
    likelihood inference, and simulation. hhh4() estimates models for
    (multivariate) count time series following Paul and Held (2011)
    <doi:10.1002/sim.4177> and Meyer and Held (2014) <doi:10.1214/14-AOAS743>.
    twinSIR() models the susceptible-infectious-recovered (SIR) event
    history of a fixed population, e.g, epidemics across farms or networks,
    as a multivariate point process as proposed by Hoehle (2009)
    <doi:10.1002/bimj.200900050>. twinstim() estimates self-exciting point
    process models for a spatio-temporal point pattern of infective events,
    e.g., time-stamped geo-referenced surveillance data, as proposed by
    Meyer et al. (2012) <doi:10.1111/j.1541-0420.2011.01684.x>.
    A recent overview of the implemented space-time modeling frameworks
    for epidemic phenomena is given by Meyer et al. (2017)
    <doi:10.18637/jss.v077.i11>.
	"""
	
	homepage = "https://surveillance.R-Forge.R-project.org/"
	cran = "surveillance" 

	version("1.22.1", md5="4dfa2580e91184b445b74930ee0979cf")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-sp@1.0.15:", type=("build", "run"))
	depends_on("r-xtable@1.7.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-polycub", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
