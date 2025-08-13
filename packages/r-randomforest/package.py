# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomforest(RPackage):
	"""Breiman and Cutler's Random Forests for Classification and Regression.

	Classification and regression based on a forest of trees using random
	inputs."""

	cran = "randomForest"
	version("4.7-1.1", sha256="f59ea87534480edbcd6baf53d7ec57e8c69f4532c2d2528eacfd48924efa2cd6")
	version("4.6-14", sha256="f4b88920419eb0a89d0bc5744af0416d92d112988702dc726882394128a8754d")
	version("4.6-12", sha256="6e512f8f88a51c01a918360acba61f1f39432f6e690bc231b7864218558b83c4")

	depends_on("r@4.1:", type=("build", "run"))


	# R 4.5 removed legacy Calloc/Free macros from public headers.
	# Replace legacy macros with new API and include proper header.
	def patch(self):
		insertion = "#include <R_ext/Memory.h>\n"

		files = [
			"src/classTree.c",
			"src/regTree.c",
			"src/rfutils.c",
			"src/regrf.c",
		]

		for relpath in files:
			# Replace legacy macros with the new API names
			filter_file(r"\\bCalloc\\(", "R_Calloc(", relpath, string=True)
			filter_file(r"\\bFree\\(", "R_Free(", relpath, string=True)
			# Ensure we include the new memory header once
			inserted = filter_file(
				r"(^#include <R.h>\\s*$)",
				r"\\1\n" + insertion,
				relpath,
				string=True,
			)
			if inserted == 0:
				# Fallback: inject after Rinternals.h if R.h pattern did not match
				filter_file(
					r"(^#include <Rinternals.h>\\s*$)",
					r"\\1\n" + insertion,
					relpath,
					string=True,
				)
