# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRds(RPackage):
	"""Respondent-Driven Sampling

	Provides functionality for carrying out estimation
    with data collected using Respondent-Driven Sampling. This includes
    Heckathorn's RDS-I and RDS-II estimators as well as Gile's Sequential
    Sampling estimator. The package is part of the "RDS Analyst" suite of
    packages for the analysis of respondent-driven sampling data.
    See Gile and Handcock (2010) <doi:10.1111/j.1467-9531.2010.01223.x>, 
    Gile and Handcock (2015) <doi:10.1111/rssa.12091> and
    Gile and Beaudry and Handcock and Ott (2018) <doi:10.1146/annurev-statistics-031017-100704>.
	"""
	
	homepage = "https://hpmrg.org"
	cran = "RDS" 

	version("0.9-9", md5="b64c1ff77c74130d829855801cdbf918")

	depends_on("r@2.5.1:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-anytime", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-statnet-common", type=("build", "run"))
	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-isotone", type=("build", "run"))
