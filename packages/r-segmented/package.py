# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSegmented(RPackage):
	"""Regression Models with Break-Points / Change-Points Estimation.

	Given a regression model, segmented 'updates' it by adding one or more
	segmented (i.e., piece-wise linear) relationships. Several variables with
	multiple breakpoints are allowed. The estimation method is discussed in
	Muggeo (2003, <doi:10.1002/sim.1545>) and illustrated in Muggeo (2008,
	<https://www.r-project.org/doc/Rnews/Rnews_2008-1.pdf>). An approach for
	hypothesis testing is presented in Muggeo (2016,
	<doi:10.1080/00949655.2016.1149855>), and interval estimation for the
	breakpoint is discussed in Muggeo (2017, <doi:10.1111/anzs.12200>)."""

	cran = "segmented"

	version("2.0-3", md5="1ea139e06c62456571430a62cc3cbc8b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
