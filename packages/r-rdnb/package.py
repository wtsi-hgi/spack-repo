# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdnb(RPackage):
	"""R Interface to the 'Deutsche Nationalbibliothek (German National
Library) API'

	A wrapper for the 'Deutsche Nationalbibliothek (German National
    Library) API', available at <https://www.dnb.de/EN/Home/home_node.html>. 
    The German National Library is the German central archival library, 
    collecting, archiving, bibliographically classifying all German and 
    German-language publications, foreign publications about Germany, 
    translations of German works, and the works of German-speaking emigrants 
    published abroad between 1933 and 1945.
	"""
	
	homepage = "https://github.com/chgrl/rdnb"
	cran = "rdnb" 

	version("0.1-5", md5="040e67c46701714cb3730664364c6529")

	depends_on("r-brew", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
