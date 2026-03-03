# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVares(RPackage):
	"""Computes Value at Risk and Expected Shortfall for over 100
Parametric Distributions

	Computes Value at risk and expected shortfall, two most popular measures of financial risk, for over one hundred parametric distributions, including all commonly known distributions.  Also computed are the corresponding probability density function and cumulative distribution function. See Chan, Nadarajah and Afuecheta (2015) <doi:10.1080/03610918.2014.944658> for more details.
	"""
	
	cran = "VaRES" 

	version("1.0.2", md5="adfe64d78b139f1eade0df581c11c7ec")

	depends_on("r@2.15:", type=("build", "run"))
