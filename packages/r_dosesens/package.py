# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDosesens(RPackage):
	"""Conduct Sensitivity Analysis with Continuous Exposures and
Binary Outcomes

	Performs sensitivity analysis for the sharp null and attributable effects in matched studies with continuous exposures and binary outcomes as described in Zhang, Small, Heng (2024) <arXiv:2401.06909>. Two of the functions require installation of the 'Gurobi' optimizer. Please see <https://www.gurobi.com/documentation/9.0/refman/ins_the_r_package.html> for guidance.
	"""
	
	cran = "doseSens" 

	version("0.1.0", md5="ec3f7ac0914d537c1331a54ea7700ac6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
