# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsogeochem(RPackage):
	"""Tools for Stable Isotope Geochemistry

	
    This toolbox makes working with oxygen,
    carbon, and clumped isotope data reproducible and straightforward.
    Use it to quickly calculate isotope fractionation factors,
    and apply paleothermometry equations.
	"""
	
	homepage = "https://davidbajnai.github.io/isogeochem/"
	cran = "isogeochem" 

	version("1.1.1", md5="8e35d2631145afb731e252f30e3db4bc")

	depends_on("r@3.1:", type=("build", "run"))
