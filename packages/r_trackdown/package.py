# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrackdown(RPackage):
	"""Collaborative Editing of Rmd (or Rnw) Documents in Google Drive

	Collaborative writing and editing of R Markdown (or Sweave) documents. The local .Rmd (or .Rnw) is uploaded as a plain-text file to Google Drive. By taking advantage of the easily readable Markdown (or LaTeX) syntax and the well-known online interface offered by Google Docs, collaborators can easily contribute to the writing and editing process. After integrating all authors’ contributions, the final document can be downloaded and rendered locally.
	"""
	
	homepage = "https://github.com/claudiozandonella/trackdown/"
	cran = "trackdown" 

	version("1.1.1", md5="f5f5e96f6b8f180f6dd2342faf8c37a0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-googledrive@1.0.1:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
