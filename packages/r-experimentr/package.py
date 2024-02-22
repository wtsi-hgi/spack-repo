# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExperimentr(RPackage):
	"""Datasets Used in Social Science Experiments: A Hands-on
Introduction

	Contains all the datasets that were used in Social Science Experiments: A Hands-On Introduction and in its R Companion. Relevant materials can be found at <https://osf.io/b78je>.
	"""
	
	cran = "experimentr" 

	version("0.1.0", md5="b3571c69440b145580b25be3fb4b1b3b")

	depends_on("r@3.50:", type=("build", "run"))
