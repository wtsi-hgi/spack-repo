# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPubtatordb(RPackage):
	"""Create and Query a Local 'PubTator' Database

	'PubTator' <https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/PubTator/> is a National Center for Biotechnology Information (NCBI) tool that enhances the annotation of articles on PubMed <https://www.ncbi.nlm.nih.gov/pubmed/>. It makes it possible to rapidly identify potential relationships between genes or proteins using text mining techniques. In contrast, manually searching for and reading the annotated articles would be very time consuming. 'PubTator' offers both an online interface and a RESTful API, however, neither of these approaches are well suited for frequent, high-throughput analyses. The package 'pubtatordb' provides a set of functions that make it easy for the average R user to download 'PubTator' annotations, create, and then query a local version of the database.
	"""
	
	cran = "pubtatordb" 

	version("0.1.4", md5="8fc4b9d4736c4b2d8c8b9b5ff7ccd971")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
