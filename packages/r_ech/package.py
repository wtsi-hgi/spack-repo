# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REch(RPackage):
	"""Downloading and Processing Microdata from ECH-INE (Uruguay)

	A consistent tool for downloading ECH data, processing them and generating new indicators: poverty, education, employment, etc. All data are downloaded from the official site of the National Institute of Statistics at <https://www.gub.uy/instituto-nacional-estadistica/datos-y-estadisticas/encuestas/encuesta-continua-hogares>.
	"""
	
	cran = "ech" 

	version("0.1.3", md5="342f258da56c8ab7c4253db32336ac65")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-geouy", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-haven@2.3:", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-laeken", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-srvyr@0.4:", type=("build", "run"))
	depends_on("r-statar", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("unrar", type=("build", "link", "run"))
	depends_on("gdal@3.0.2:", type=("build", "link", "run"))
	depends_on("geos@3.8.0:", type=("build", "link", "run"))
	depends_on("proj@6.2.1:", type=("build", "link", "run"))
