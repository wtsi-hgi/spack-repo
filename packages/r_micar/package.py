# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicar(RPackage):
	"""'Mica' Data Web Portal Client

	'Mica' is a server application used to create data web portals for 
    large-scale epidemiological studies or multiple-study consortia. 'Mica' helps
    studies to provide scientifically robust data visibility and web presence 
    without significant information technology effort. 'Mica' provides a 
    structured description of consortia, studies, annotated and searchable data
    dictionaries, and data access request management. This 'Mica' client allows
    to perform data extraction for reporting purposes.
	"""
	
	homepage = "https://www.obiba.org/"
	cran = "micar" 

	version("1.1.2", md5="3ce5592504a680ca967b8aebed022c80")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
