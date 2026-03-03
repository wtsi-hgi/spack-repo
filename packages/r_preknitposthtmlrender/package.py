# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPreknitposthtmlrender(RPackage):
	"""Pre-Knitting Processing and Post HTML-Rendering Processing

	Dynamize headers or R code within 'Rmd' files to prevent proliferation of 'Rmd' files for similar reports. Add in external HTML document within 'rmarkdown' rendered HTML doc.
	"""
	
	homepage = "https://github.com/chinsoon12/PreKnitPostHTMLRender"
	cran = "PreKnitPostHTMLRender" 

	version("0.1.0", md5="162c9d2f404bd556bc3a476d83cff0ea")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-xml@3.98.1.4:", type=("build", "run"))
	depends_on("r-knitr@1.13:", type=("build", "run"))
	depends_on("r-rmarkdown@0.9.6:", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
