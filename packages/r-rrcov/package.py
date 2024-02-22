# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrcov(RPackage):
	"""Scalable Robust Estimators with High Breakdown Point.

	Robust Location and Scatter Estimation and Robust Multivariate Analysis
	with High Breakdown Point: principal component analysis (Filzmoser and
	Todorov (2013), <doi:10.1016/j.ins.2012.10.017>), linear and quadratic
	discriminant analysis (Todorov and Pires (2007)), multivariate tests
	(Todorov and Filzmoser (2010) <doi:10.1016/j.csda.2009.08.015>), outlier
	detection (Todorov et al. (2010) <doi:10.1007/s11634-010-0075-2>). See also
	Todorov and Filzmoser (2009) <ISBN-13:978-3838108148>, Todorov and
	Filzmoser (2010) <doi:10.18637/jss.v032.i03> and Boudt et al. (2019)
	<doi:10.1007/s11222-019-09869-x>."""

	cran = "rrcov"

	version("1.7-5", md5="8cadc312f7a778a807e7c29716c14d65")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-robustbase@0.92.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
