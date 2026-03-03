# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSp2000(RPackage):
	"""Catalogue of Life Toolkit

	A programmatic interface to <http://sp2000.org.cn>, re-written based on an accompanying 'Species 2000' API. Access tables describing catalogue of the Chinese known species of animals, plants, fungi, micro-organisms, and more. This package also supports access to catalogue of life global <http://catalogueoflife.org>, China animal scientific database <http://zoology.especies.cn> and catalogue of life Taiwan <https://taibnet.sinica.edu.tw/home_eng.php>. The development of 'SP2000' package were supported by Biodiversity Survey and Assessment Project of the Ministry of Ecology and Environment, China <2019HJ2096001006>,Yunnan University's "Double First Class" Project <C176240405> and Yunnan University's Research Innovation Fund for Graduate Students <2019227>.
	"""
	
	homepage = "https://otoliths.github.io/SP2000/"
	cran = "SP2000" 

	version("0.2.0", md5="782d0804e50cf8d86193de6b3b9b7cfb", url="https://cran.r-project.org/src/contrib/SP2000_0.2.0.tar.gz")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
