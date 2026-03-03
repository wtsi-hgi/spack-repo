# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebshot2(RPackage):
	"""Take Screenshots of Web Pages

	Takes screenshots of web pages, including Shiny applications
    and R Markdown documents. 'webshot2' uses headless Chrome or Chromium
    as the browser back-end.
	"""
	
	homepage = "https://rstudio.github.io/webshot2/"
	cran = "webshot2" 

	version("0.1.1", md5="0f383d41d9f6453ab252016dabdebc2d", url="https://cran.r-project.org/src/contrib/webshot2_0.1.1.tar.gz")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-chromote@0.1:", type=("build", "run"))
	depends_on("r-later", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-promises", type=("build", "run"))
