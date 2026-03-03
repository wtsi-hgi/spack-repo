# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeopleanalyticsdata(RPackage):
	"""Data Sets for Keith McNulty's Handbook of Regression Modeling in
People Analytics

	Data sets for statistical inference modeling related to People Analytics.  
  Contains various data sets from the book 'Handbook of Regression Modeling in People Analytics' 
  by Keith McNulty (2020).
	"""
	
	homepage = "http://peopleanalytics-regression-book.org"
	cran = "peopleanalyticsdata" 

	version("0.2.1", md5="24e8be670a117fb22abb48b6757e11e5")

	depends_on("r@2.10:", type=("build", "run"))
