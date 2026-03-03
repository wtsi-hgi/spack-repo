# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRasciidoc(RPackage):
	"""Create Reports Using R and 'asciidoc'

	Inspired by Karl Broman`s reader on using 'knitr'
    with 'asciidoc'
    (<https://kbroman.org/knitr_knutshell/pages/asciidoc.html>), this is
    merely a wrapper to 'knitr' and 'asciidoc'.
	"""
	
	homepage = "https://gitlab.com/fvafrcu/rasciidoc"
	cran = "rasciidoc" 

	version("4.1.1", md5="8fd375b7a9913526df5d19329904aa11")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-fritools@3.7.1:", type=("build", "run"))
	depends_on("r-gert", type=("build", "run"))
	depends_on("r-highr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("python@2.6:", type=("build", "link", "run"))
	depends_on("asciidoc", type=("build", "link", "run"))
