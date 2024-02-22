# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPersonr(RPackage):
	"""Test Your Personality

	An R-package-version of an open online science-based personality
    test from <https://openpsychometrics.org/tests/IPIP-BFFM/>,
    providing a better-designed interface and a more detailed report.
    The core command launch_test() opens a personality test in your browser,
    and generates a report after you click "Submit". In this report, your results
    are compared with other people's, to show what these results mean.
    Other people's data is from <https://openpsychometrics.org/_rawdata/BIG5.zip>.
	"""
	
	homepage = "https://github.com/flujoo/personr"
	cran = "personr" 

	version("1.0.0", md5="41bde1ac25a2b9f376a75cea61ff0a41")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
