# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnadata(RPackage):
	"""Data Sets for Keith McNulty's Handbook of Graphs and Networks in
People Analytics

	Data sets for network analysis related to People Analytics.  
  Contains various data sets from the book 'Handbook of Graphs and Networks in People Analytics' 
  by Keith McNulty (2021).
	"""
	
	homepage = "https://ona-book.org"
	cran = "onadata" 

	version("0.1", md5="79156613883fa7f36147b00c072edd3b")

	depends_on("r@2.10:", type=("build", "run"))
