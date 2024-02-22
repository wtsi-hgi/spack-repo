# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScientotext(RPackage):
	"""Text & Scientometric Analytics

	It involves bibliometric indicators calculation from bibliometric data.It also deals pattern analysis using the text part of bibliometric data.The bibliometric data are obtained from mainly Web of Science and Scopus.
	"""
	
	cran = "scientoText" 

	version("0.1", md5="10b68e1521707983d96946a052e38db1")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
