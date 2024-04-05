# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrutiny(RPackage):
	"""Error Detection in Science

	Test published summary statistics for consistency
    (Brown and Heathers, 2017, <doi:10.1177/1948550616673876>;
    Allard, 2018, <https://aurelienallard.netlify.app/post/anaytic-grimmer-possibility-standard-deviations/>;
    Heathers and Brown, 2019, <https://osf.io/5vb3u/>).
    The package also provides infrastructure for implementing new
    error detection techniques.
	"""
	
	homepage = "https://lhdjung.github.io/scrutiny/"
	cran = "scrutiny" 

	version("0.4.0", md5="22fe7e6d3b30922fe412c514d37002af")
	version("0.3.0", md5="f3f390603f13e976c0a0b1fb02d12630")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-corrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.0.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
