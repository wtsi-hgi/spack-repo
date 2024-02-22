# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPatchsynctex(RPackage):
	"""Communication Between Editor and Viewer for Literate Programs

	This utility eases the debugging of literate documents
	     ('noweb' files) by patching the synchronization information
	     (the '.synctex(.gz)' file) produced by 'pdflatex' with
	     concordance information produced by 'Sweave' or 'knitr' and
	     'Sweave' or 'knitr' ; this allows for bilateral communication
	     between a text editor (visualizing the 'noweb' source) and
	     a viewer (visualizing the resultant 'PDF'), thus bypassing
	     the intermediate 'TeX' file.
	"""
	
	homepage = "https://github.com/EmmanuelCharpentier/patchSynctex"
	cran = "patchSynctex" 

	version("0.1-4", md5="dc9304a7698a7edcfd1cf54002cde8c7")

	depends_on("r-stringr", type=("build", "run"))
