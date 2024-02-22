# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInpdfr(RPackage):
	"""Analyse Text Documents Using Ecological Tools

	A set of functions to analyse and compare texts, using classical 
  text mining	functions, as well as those from theoretical ecology.
	"""
	
	homepage = "https://github.com/frareb/inpdfr/"
	cran = "inpdfr" 

	version("0.1.12", md5="d261489f29f65edf63ba915969bd6793")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-wordcloud@2.5:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-tm@0.6.2:", type=("build", "run"))
	depends_on("r-snowballc@0.5.1:", type=("build", "run"))
	depends_on("r-cluster@2.0.1:", type=("build", "run"))
	depends_on("r-entropart@1.4.1:", type=("build", "run"))
	depends_on("r-metacom@1.4.4:", type=("build", "run"))
	depends_on("r-stringi@1.0.1:", type=("build", "run"))
	depends_on("r-r-devices@2.14:", type=("build", "run"))
