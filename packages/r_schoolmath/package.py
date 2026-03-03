# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSchoolmath(RPackage):
	"""Functions and Datasets for Math Used in School

	Contains functions and datasets for math taught in school. A main focus is set to prime-calculation.
	"""
	
	cran = "schoolmath" 

	version("0.4.2", md5="d737df347c95ffc69300b75cb50447a1")

	depends_on("r@2.10:", type=("build", "run"))
