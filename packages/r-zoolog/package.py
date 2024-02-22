# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZoolog(RPackage):
	"""Zooarchaeological Analysis with Log-Ratios

	Includes functions and reference data to 
    generate and manipulate log-ratios (also known as log size index (LSI)
    values) from measurements obtained on zooarchaeological material. Log
    ratios are used to compare the relative (rather than the absolute)
    dimensions of animals from archaeological contexts 
    (Meadow 1999, ISBN: 9783896463883).
    zoolog is also able to seamlessly integrate data and references 
    with heterogeneous nomenclature, which is internally managed by a 
    zoolog thesaurus. 
    A preliminary version of the zoolog methods was first used by 
    Trentacoste, Nieto-Espinet, and Valenzuela-Lamas (2018) 
    <doi:10.1371/journal.pone.0208109>.
	"""
	
	homepage = "https://josempozo.github.io/zoolog/"
	cran = "zoolog" 

	version("1.1.0", md5="56e72a52f69bc89f793cdf6fa07c5bf2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
