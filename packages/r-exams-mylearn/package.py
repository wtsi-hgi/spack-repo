# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExamsMylearn(RPackage):
	"""Question Generation in the 'MyLearn' XML Format

	Randomized multiple-select and single-select
  question generation for the 'MyLearn' teaching and learning
  platform. Question templates
  in the form of the R/exams package (see <http://www.r-exams.org/>)
  are transformed into XML format required by 'MyLearn'.
	"""
	
	homepage = "https://github.com/hdarjus/exams.mylearn"
	cran = "exams.mylearn" 

	version("1.4", md5="648b35f6d75eaf2c40abf6d2a68c4526")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-exams@2.3.4:", type=("build", "run"))
	depends_on("r-glue@1.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-stringi@1.4.6:", type=("build", "run"))
	depends_on("r-pkgbuild@1.1:", type=("build", "run"))
	depends_on("r-xml2@1.2.5:", type=("build", "run"))
