# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKonpsurv(RPackage):
	"""KONP Tests: Powerful K-Sample Tests for Right-Censored Data

	The K-sample omnibus non-proportional hazards (KONP) tests are powerful non-parametric tests for comparing K (>=2) hazard functions based on right-censored data (Gorfine, Schlesinger and Hsu, 2020, <doi:10.1177/0962280220907355>). These tests are consistent against any differences between the hazard functions of the groups. The KONP tests are often more powerful than other existing tests, especially under non-proportional hazard functions.
	"""
	
	cran = "KONPsurv" 

	version("1.0.4", md5="4198005da82d348f44e49ec2a558e675")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
