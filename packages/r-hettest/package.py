# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHettest(RPackage):
	"""Testing for a Treatment Effect Using a Heterogeneous Surrogate
Marker

	Tests for a treatment effect using surrogate marker information accounting for heterogeneity in the utility of the surrogate. Details are described in Parast et al (2022) <arXiv:2209.08315>.
	"""
	
	cran = "hettest" 

	version("1.0", md5="ef516e0342a60e7f940faab02842a76a")

	depends_on("r@3.5:", type=("build", "run"))
