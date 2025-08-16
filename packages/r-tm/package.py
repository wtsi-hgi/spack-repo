# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTm(RPackage):
	"""Text Mining Package

	A framework for text mining applications within R.
	"""
	
	homepage = "https://tm.r-forge.r-project.org/"
	cran = "tm" 

	version("0.7-12", md5="60d60d1df2964cedeccddf60eccd66e4")
	version("0.7-11", md5="2634a0ba7621014348a89f156837ad31")

	# R 4.5 removed legacy Calloc/Realloc/Free macros. Apply in-place edits.
	def patch(self):
		# Ensure modern RS.h macros are available and replace deprecated calls
		filter_file("#include <Rdefines.h>",
		            "#include <Rdefines.h>\n#include <R_ext/RS.h>",
		            "src/scan.c")
		# Replace removed Calloc/Realloc/Free with R_Calloc/R_Realloc/R_Free
		filter_file(r"\bCalloc\(", "R_Calloc(", "src/scan.c")
		filter_file(r"\bRealloc\(", "R_Realloc(", "src/scan.c")
		filter_file(r"\bFree\(", "R_Free(", "src/scan.c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-nlp@0.2.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-slam@0.1.37:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
