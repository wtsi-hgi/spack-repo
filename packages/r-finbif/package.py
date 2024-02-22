# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinbif(RPackage):
	"""Interface for the 'Finnish Biodiversity Information Facility'
API

	A programmatic interface to the 'Finnish Biodiversity Information
    Facility' ('FinBIF') API (<https://api.laji.fi>). 'FinBIF' aggregates
    Finnish biodiversity data from multiple sources in a single open access
    portal for researchers, citizen scientists, industry and government.
    'FinBIF' allows users of biodiversity information to find, access, combine
    and visualise data on Finnish plants, animals and microorganisms. The
    'finbif' package makes the publicly available data in 'FinBIF' easily
    accessible to programmers. Biodiversity information is available on taxonomy
    and taxon occurrence. Occurrence data can be filtered by taxon, time,
    location and other variables. The data accessed are conveniently
    preformatted for subsequent analyses.
	"""
	
	homepage = "https://github.com/luomus/finbif"
	cran = "finbif" 

	version("0.9.4", md5="a3d1e91df18baacb2dfaad641b304664")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lutz", type=("build", "run"))
