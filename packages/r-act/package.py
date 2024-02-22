# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAct(RPackage):
	"""Aligned Corpus Toolkit

	The Aligned Corpus Toolkit (act) is designed for linguists that work with time aligned transcription data. It offers functions to import and export various annotation file formats ('ELAN' .eaf, 'EXMARaLDA .exb and 'Praat' .TextGrid files), create print transcripts in the style of conversation analysis, search transcripts (span searches across multiple annotations, search in normalized annotations, make concordances etc.), export and re-import search results (.csv and 'Excel' .xlsx format), create cuts for the search results (print transcripts, audio/video cuts using 'FFmpeg' and video sub titles in 'Subrib title' .srt format), modify the data in a corpus (search/replace, delete, filter etc.), interact with 'Praat' using 'Praat'-scripts, and exchange data with the 'rPraat' package. The package is itself written in R and may be expanded by other users.
	"""
	
	homepage = "http://www.oliverehmer.de"
	cran = "act" 

	version("1.3.1", md5="05eec7e34f11181b3dd68db70fa11c4c")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-textutils", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
