# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAltdoc(RPackage):
	"""Package Documentation Websites with 'Quarto', 'Docsify',
'Docute', or 'MkDocs'

	This is a simple and powerful package to create, render, preview, 
    and deploy documentation websites for 'R' packages. It is a lightweight and 
    flexible alternative to 'pkgdown', with support for many documentation 
    generators, including 'Quarto', 'Docute', 'Docsify', and 'MkDocs'.
	"""
	
	homepage = "https://altdoc.etiennebacher.com"
	cran = "altdoc" 

	version("0.3.0", md5="4f4ad0c76e872e8322618253ed940777")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-quarto", type=("build", "run"))
