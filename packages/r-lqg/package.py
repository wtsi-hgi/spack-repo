# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLqg(RPackage):
	"""Robust Group Variable Screening Based on Maximum Lq-Likelihood
Estimation

	Produces a group screening procedure that is based on maximum Lq-likelihood estimation, to simultaneously account for the group structure and data contamination in variable screening. The methods are described in Li, Y., Li, R., Qin, Y., Lin, C., & Yang, Y. (2021) Robust Group Variable Screening Based on Maximum Lq-likelihood Estimation. Statistics in Medicine, 40:6818-6834.<doi:10.1002/sim.9212>.
	"""
	
	cran = "LqG" 

	version("0.1.0", md5="109bfd68988e73bb76a6533f7f25d4e8")

	depends_on("r@3.5:", type=("build", "run"))
