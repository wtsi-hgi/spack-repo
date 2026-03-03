# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeddlr(RPackage):
	"""Dynamic R Markdown Document Generation

	Helper functions designed to make
    dynamically generating R Markdown documents easier by providing a
    simple and tidy way to create report pieces, shape them to your data,
    and combine them for exporting into a single R Markdown document.
	"""
	
	homepage = "https://github.com/mikemahoney218/heddlr"
	cran = "heddlr" 

	version("0.6.0", md5="384942b99e49803634a1815bdb2ad9c4")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-utf8", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
