# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSspse(RPackage):
	"""Estimating Hidden Population Size using Respondent Driven
Sampling Data

	Estimate the size of a networked population based on
    respondent-driven sampling data. The package is part of the "RDS Analyst"
    suite of packages for the analysis of respondent-driven sampling data.
    See Handcock, Gile and Mar (2014) <doi:10.1214/14-EJS923>,
    Handcock, Gile and Mar (2015) <doi:10.1111/biom.12255>,
    Kim and Handcock (2021) <doi:10.1093/jssam/smz055>, and
    McLaughlin, et. al. (2023) <doi:10.1214/23-AOAS1807>.
	"""
	
	homepage = "https://hpmrg.org"
	cran = "sspse" 

	version("1.1.0-1", md5="d9e6c92c31bf2d30eab81580e4035ffd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rds", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-scam", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
