# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAirr(RPackage):
	"""AIRR Data Representation Reference Library

	Schema definitions and read, write and validation tools for data 
    formatted in accordance with the AIRR Data Representation schemas defined 
    by the AIRR Community <http://docs.airr-community.org>.
	"""
	
	homepage = "http://docs.airr-community.org"
	cran = "airr" 

	version("1.5.0", md5="9e4729ed604fc3d017223dc675504fb9")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
