# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROottest(RPackage):
	"""Out-of-Treatment Testing

	Implements the out-of-treatment testing from Kuelpmann and Kuzmics (2020) <doi:10.2139/ssrn.3441675> based on the Vuong Test introduced in Vuong (1989) <doi:10.2307/1912557>. 
    Out-of treatment testing allows for a direct, pairwise likelihood comparison of theories, calibrated with pre-existing data.
	"""
	
	homepage = "https://github.com/PhilippKuelpmann/oottest"
	cran = "oottest" 

	version("0.9.1", md5="045a6d462baf9f2e5e71c42b5e3f91ee")

	depends_on("r@3.5:", type=("build", "run"))
