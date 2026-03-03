# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrmbigdata(RPackage):
	"""Fitting Semiparametric Cumulative Probability Models for Big
Data

	A big data version for fitting cumulative probability models using the orm() function.  See Liu et al. (2017) <DOI:10.1002/sim.7433> for details.
	"""
	
	cran = "ormBigData" 

	version("0.0.1", md5="af0751e89fe3eca183232843f51a0fed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rms@5.1.4:", type=("build", "run"))
	depends_on("r-hmisc@4.3.0:", type=("build", "run"))
	depends_on("r-doparallel@1.0.11:", type=("build", "run"))
	depends_on("r-foreach@1.2:", type=("build", "run"))
	depends_on("r-iterators@1:", type=("build", "run"))
	depends_on("r-sparsem@1.77:", type=("build", "run"))
	depends_on("r-benchmarkme@1.0.4:", type=("build", "run"))
