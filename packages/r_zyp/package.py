# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZyp(RPackage):
	"""Zhang + Yue-Pilon Trends Package

	An efficient implementation of the slope method described by Sen (1968) <doi:10.1080/01621459.1968.10480934> plus implementation of prewhitening approaches to determining trends in climate data described by Zhang, Vincent, Hogg, and Niitsoo (2000) <doi:10.1080/07055900.2000.9649654> and Yue, Pilon, Phinney, and Cavadias (2002) <doi:10.1002/hyp.1095>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "zyp" 

	version("0.11-1", md5="7dc344086f71cc93d29e80eccd15a588")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-kendall", type=("build", "run"))
