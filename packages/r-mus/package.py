# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMus(RPackage):
	"""Monetary Unit Sampling and Estimation Methods, Widely Used in
Auditing

	Sampling and evaluation methods to apply Monetary Unit Sampling (or in older literature Dollar Unit Sampling) during an audit of financial statements.
	"""
	
	cran = "MUS" 

	version("0.1.6", md5="ff9dda815a29881a16a55986440bdd96")

	depends_on("r@3.4:", type=("build", "run"))
