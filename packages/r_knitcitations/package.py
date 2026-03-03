# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnitcitations(RPackage):
	"""Citations for 'Knitr' Markdown Files

	Provides the ability to create dynamic citations
    in which the bibliographic information is pulled from the web rather
    than having to be entered into a local database such as 'bibtex' ahead of
    time. The package is primarily aimed at authoring in the R 'markdown'
    format, and can provide outputs for web-based authoring such as linked
    text for inline citations.  Cite using a 'DOI', URL, or
    'bibtex' file key.  See the package URL for details.
	"""
	
	homepage = "https://github.com/cboettig/knitcitations"
	cran = "knitcitations" 

	version("1.0.12", md5="da9d2629844dc25417abdc92e581e2e5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-refmanager@0.8.2:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr@0.3:", type=("build", "run"))
