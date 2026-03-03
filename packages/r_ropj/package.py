# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRopj(RPackage):
	"""Import Origin(R) Project Files

	Read the data from Origin(R) project files ('*.opj')
	<https://www.originlab.com/doc/User-Guide/Origin-File-Types>.
	No write support is planned.
	"""
	
	homepage = "https://github.com/aitap/Ropj"
	cran = "Ropj" 

	version("0.3-5", md5="fdfdc3384b53c187dd3832a1c57cf1c3")
	version("0.3-4", md5="8359e79f5d8d37373822a22730165063")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
