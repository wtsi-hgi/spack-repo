# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMemoir(RPackage):
	"""R Markdown and Bookdown Templates to Publish Documents

	Producing high-quality documents suitable for publication directly from R is made possible by the R Markdown ecosystem.
  'memoiR' makes it easy.
  It provides templates to knit memoirs, articles and slideshows with helpers to publish the documents on GitHub Pages and activate continuous integration.
	"""
	
	homepage = "https://github.com/EricMarcon/memoiR"
	cran = "memoiR" 

	version("1.2-4", md5="b65a3524626774398d0d24de5e1882cc")

	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-distill", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rmdformats", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
