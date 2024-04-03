# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSomadataio(RPackage):
	"""Input/Output 'SomaScan' Data

	Load and export 'SomaScan' data via the
    'SomaLogic Operating Co., Inc.' structured text file
    called an ADAT ('*.adat'). For file format see
    <https://github.com/SomaLogic/SomaLogic-Data/blob/master/README.md>.
    The package also exports auxiliary functions for
    manipulating, wrangling, and extracting relevant
    information from an ADAT object once in memory.
	"""
	
	homepage = "https://somalogic.github.io/SomaDataIO/"
	cran = "SomaDataIO" 

	version("6.1.0", md5="efa032745f828e272df22f1025d511bc")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-lifecycle@1:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
	depends_on("r-tibble@3.1.2:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
	depends_on("r-usethis@2.0.1:", type=("build", "run"))
