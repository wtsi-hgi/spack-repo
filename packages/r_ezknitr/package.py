# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REzknitr(RPackage):
	"""Avoid the Typical Working Directory Pain When Using 'knitr'

	An extension of 'knitr' that adds flexibility in several
    ways. One common source of frustration with 'knitr' is that it assumes
    the directory where the source file lives should be the working directory,
    which is often not true. 'ezknitr' addresses this problem by giving you
    complete control over where all the inputs and outputs are, and adds several
    other convenient features to make rendering markdown/HTML documents easier.
	"""
	
	homepage = "https://docs.ropensci.org/ezknitr/"
	cran = "ezknitr" 

	version("0.6.3", md5="d9ba1ab3acdc6559cf954fe40b335f5e")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-knitr@1.7:", type=("build", "run"))
	depends_on("r-markdown@0.7:", type=("build", "run"))
	depends_on("r-r-utils@1.34:", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
