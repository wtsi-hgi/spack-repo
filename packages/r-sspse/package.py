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
    See Handcock, Gile and Mar (2014) <doi:10.1214/14-EJS923> and
    Handcock, Gile and Mar (2015) <doi:10.1111/biom.12255>.
	"""
	
	homepage = "https://hpmrg.org"
	cran = "sspse" 

	version("1.1.0", md5="27ddfa0751ff5f579d8a785ae9aab27e")

	depends_on("r-rds", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-scam", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
