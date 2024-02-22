# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadxlsb(RPackage):
	"""Read 'Excel' Binary (.xlsb) Workbooks

	Import data from 'Excel' binary (.xlsb) workbooks into R.
	"""
	
	homepage = "https://github.com/velofrog/readxlsb"
	cran = "readxlsb" 

	version("0.1.61", md5="2379846e16021a5ba52f46d3ddfef72e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-cellranger", type=("build", "run"))
