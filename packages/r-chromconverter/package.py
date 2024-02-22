# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromconverter(RPackage):
	"""Chromatographic File Converter

	Reads chromatograms from binary formats into R objects. Currently supports conversion of 'Agilent ChemStation', 'Agilent MassHunter', and 'ThermoRaw' files as well as various text-based formats. Utilizes file parsers from external libraries, such as 'Aston' <https://github.com/bovee/aston>, 'Entab' <https://github.com/bovee/entab>, and 'ThermoRawFileParser' <https://github.com/compomics/ThermoRawFileParser>.
	"""
	
	homepage = "https://github.com/ethanbass/chromConverter"
	cran = "chromConverter" 

	version("0.2.1", md5="9c83a95900cb250c56682b9431c82aae")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
