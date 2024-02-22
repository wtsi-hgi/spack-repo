# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPandoc(RPackage):
	"""Manage and Run Universal Converter 'Pandoc' from 'R'

	Provides a set of tools to install, manage and run several
    'Pandoc' versions.
	"""
	
	homepage = "https://github.com/cderv/pandoc"
	cran = "pandoc" 

	version("0.2.0", md5="3afcf6c2a93adc983933651fe1a23406")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang@1.0.1:", type=("build", "run"))
