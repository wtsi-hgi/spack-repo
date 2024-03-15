# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLingtypology(RPackage):
	"""Linguistic Typology and Mapping

	Provides R with the Glottolog database <https://glottolog.org/> and some more abilities for purposes of linguistic mapping. The Glottolog database contains the catalogue of languages of the world. This package helps researchers to make a linguistic maps, using philosophy of the Cross-Linguistic Linked Data project <https://clld.org/>, which allows for while at the same time facilitating uniform access to the data across publications. A tutorial for this package is available on GitHub pages <https://docs.ropensci.org/lingtypology/> and package vignette. Maps created by this package can be used both for the investigation and linguistic teaching. In addition, package provides an ability to download data from typological databases such as WALS, AUTOTYP and some others and to create your own database website.
	"""
	
	homepage = "https://CRAN.R-project.org/package=lingtypology"
	cran = "lingtypology" 

	version("1.1.17", md5="c2c11e3c1199d490c1c7707858f3e337")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-leaflet-minicharts", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
