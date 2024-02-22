# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExams2sakai(RPackage):
	"""Automatic Generation of Exams in R for 'Sakai'

	Automatic Generation of Exams in R for 'Sakai'.
  Question templates in the form of the 'exams' package (see <http://www.r-exams.org/>)
  are transformed into XML format required by 'Sakai'.
	"""
	
	homepage = "https://github.com/jesusmmp/exams2sakai"
	cran = "exams2sakai" 

	version("0.3", md5="e5ec266a9f669b919ce573d9f42ad6e8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-exams@2.3.6:", type=("build", "run"))
	depends_on("r-glue@1.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-stringi@1.4.6:", type=("build", "run"))
	depends_on("r-xml2@1.2.5:", type=("build", "run"))
