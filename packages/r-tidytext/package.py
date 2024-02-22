# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidytext(RPackage):
	"""Text Mining using 'dplyr', 'ggplot2', and Other Tidy Tools

	Using tidy data principles can make many text mining tasks
    easier, more effective, and consistent with tools already in wide use.
    Much of the infrastructure needed for text mining with tidy data
    frames already exists in packages like 'dplyr', 'broom', 'tidyr', and
    'ggplot2'. In this package, we provide functions and supporting data
    sets to allow conversion of text to and from tidy formats, and to
    switch seamlessly between tidy tools and existing text mining
    packages.
	"""
	
	homepage = "https://github.com/juliasilge/tidytext"
	cran = "tidytext" 

	version("0.4.1", md5="a8a7ab36132d2bb8e2cb8e74d9ee1a56")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-janeaustenr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr@0.1.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tokenizers", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
