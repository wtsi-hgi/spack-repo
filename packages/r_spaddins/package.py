# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpaddins(RPackage):
	"""A Set of RStudio Addins

	A set of RStudio addins that are designed to be used in
             combination with user-defined RStudio keyboard shortcuts. These
             addins either:
             1) insert text at a cursor position (e.g. insert
             operators %>%, <<-, %$%, etc.),
             2) replace symbols in selected pieces of text (e.g., convert
             backslashes to forward slashes which results in stings like
             "c:data" converted into "c:/data/") or
             3) enclose text with special symbols (e.g., converts "bold" into
             "**bold**") which is convenient for editing R Markdown files.
	"""
	
	homepage = "https://github.com/GegznaV/spAddins"
	cran = "spAddins" 

	version("0.2.0", md5="5544deab34b4c1f468fd164767c0dd0d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
