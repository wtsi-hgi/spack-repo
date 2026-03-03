# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrrna(RPackage):
	"""Coefficients of Interrater Reliability – Generalized for
Randomly Incomplete Datasets

	Provides coefficients of interrater reliability that are generalized to cope with randomly incomplete (i.e. unbalanced) datasets without any imputation of missing values or any (row-wise or column-wise) omissions of actually available data. Applied to complete (balanced) datasets, these generalizations yield the same results as the common procedures, namely the Intraclass Correlation according to McGraw & Wong (1996) doi{10.1037/1082-989X.1.1.30} and the Coefficient of Concordance according to Kendall & Babington Smith (1939) doi{10.1214/aoms/1177732186}.
	"""
	
	homepage = "https://CRAN.R-project.org/package=irrNA"
	cran = "irrNA" 

	version("0.2.3", md5="e2c20fd55ec9230b76488785cc3a51d3")

	depends_on("r@2.10:", type=("build", "run"))
