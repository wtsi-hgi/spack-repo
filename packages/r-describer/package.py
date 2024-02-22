# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDescriber(RPackage):
	"""Describe Data in R Using Common Descriptive Statistics

	Allows users to quickly and easily describe data using
    common descriptive statistics.
	"""
	
	homepage = "https://github.com/paulhendricks/describer"
	cran = "describer" 

	version("0.2.0", md5="d2d73f45143cc46eaa0a7feb6bbb4bc7")

	depends_on("r@3.1.2:", type=("build", "run"))
