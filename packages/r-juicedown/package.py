# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJuicedown(RPackage):
	"""'juice' + 'markdown': Convert 'R Markdown' into 'HTML' with
Inline Styles

	A convenience tool to create 'HTML' with inline styles using 
  'juicyjuice' and 'markdown' packages. It is particularly useful when working 
  on a content management system (CMS) whose code editor eliminates style and 
  link tags. The main use case of the package is the learning management system, 
  'Moodle'. Additional helper functions for teaching purposes are provided. Learn 
  more about 'juicedown' at <https://kenjisato.github.io/juicedown/>.
	"""
	
	homepage = "https://kenjisato.github.io/juicedown/"
	cran = "juicedown" 

	version("0.1.1", md5="fa0cf2f4a40d36d9861214a2768e5f7d")

	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-juicyjuice", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-sass", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
