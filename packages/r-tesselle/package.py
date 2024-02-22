# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTesselle(RPackage):
	"""Easily Install and Load 'tesselle' Packages

	Easy install and load key packages from the 'tesselle' suite
    in a single step. The 'tesselle' suite is a collection of packages for
    research and teaching in archaeology. These packages focus on
    quantitative analysis methods developed for archaeology. The
    'tesselle' packages are designed to work seamlessly together and to
    complement general-purpose and other specialized statistical packages.
    These packages can be used to explore and analyze common data types in
    archaeology: count data, compositional data and chronological data.
    Learn more about 'tesselle' at <https://www.tesselle.org>.
	"""
	
	homepage = "https://github.com/tesselle/tesselle"
	cran = "tesselle" 

	version("1.4.0", md5="0247241b2f657e3c9e5d0aa732cf2760")

	depends_on("r-dimensio@0.5:", type=("build", "run"))
	depends_on("r-folio@1.3:", type=("build", "run"))
	depends_on("r-isopleuros@1:", type=("build", "run"))
	depends_on("r-kairos@2.0.2:", type=("build", "run"))
	depends_on("r-khroma@1.11:", type=("build", "run"))
	depends_on("r-nexus@0.1:", type=("build", "run"))
	depends_on("r-tabula@3.0.1:", type=("build", "run"))
