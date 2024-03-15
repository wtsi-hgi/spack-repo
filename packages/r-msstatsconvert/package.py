# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsstatsconvert(RPackage):
	"""Import Data from Various Mass Spectrometry Signal Processing Tools to MSstats Format

	MSstatsConvert provides tools for importing reports of Mass Spectrometry data processing tools into R format suitable for statistical analysis using the MSstats and MSstatsTMT packages.
	"""
	
	bioc = "MSstatsConvert" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MSstatsConvert_1.12.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MSstatsConvert/MSstatsConvert_1.12.1.tar.gz"]

	version("1.12.1", md5="d522e5ee79c371a83f959808b7c9d214")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-log4r", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
