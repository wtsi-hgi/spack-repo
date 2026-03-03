# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGt(RPackage):
	"""Easily Create Presentation-Ready Display Tables

	Build display tables from tabular data with an easy-to-use set of
    functions. With its progressive approach, we can construct display tables
    with a cohesive set of table parts. Table values can be formatted using any
    of the included formatting functions. Footnotes and cell styles can be 
    precisely added through a location targeting system. The way in which 'gt'
    handles things for you means that you don't often have to worry about the
    fine details.
	"""
	
	homepage = "https://gt.rstudio.com"
	cran = "gt" 

	version("0.10.1", md5="8e823620e16426d866bf18c9e2dc59a3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-base64enc@0.1.3:", type=("build", "run"))
	depends_on("r-bigd@0.2:", type=("build", "run"))
	depends_on("r-bitops@1.0.7:", type=("build", "run"))
	depends_on("r-cli@3.6:", type=("build", "run"))
	depends_on("r-commonmark@1.8.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-fs@1.6.1:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-htmltools@0.5.4:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.6.1:", type=("build", "run"))
	depends_on("r-juicyjuice@0.1:", type=("build", "run"))
	depends_on("r-magrittr@2.0.2:", type=("build", "run"))
	depends_on("r-markdown@1.5:", type=("build", "run"))
	depends_on("r-reactable@0.4.3:", type=("build", "run"))
	depends_on("r-rlang@1.0.2:", type=("build", "run"))
	depends_on("r-sass@0.4.5:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-xml2@1.3.3:", type=("build", "run"))
