# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsppdata(RPackage):
	"""Data Only: The Correlates of State Policy Project Dataset

	Contains the Correlates of State Policy Project dataset (+ codebook) assembled by Marty P. Jordan and Matt Grossmann (2020) <http://ippsr.msu.edu/public-policy/correlates-state-policy> used by the 'cspp' package. The Correlates data contains over 3000 variables across more than 100 years that pertain to state politics and policy in the United States.
	"""
	
	cran = "csppData" 

	version("0.2.61", md5="077133704fb3cdce6bfa04f35e61fa27")

	depends_on("r@3.50:", type=("build", "run"))
