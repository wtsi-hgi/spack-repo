# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasyahp(RPackage):
	"""Analytic Hierarchy Process (AHP)

	Given the scores from decision makers, the analytic hierarchy process can be conducted easily.
	"""
	
	cran = "easyAHP" 

	version("0.1.1", md5="8087051913bcdd47730b0c711261b02a")

