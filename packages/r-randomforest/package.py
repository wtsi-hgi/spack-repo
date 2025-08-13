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
	# Inject portable compatibility macros so the C sources continue to build.
	def patch(self):
		insertion = (
			"#include <R_ext/RS.h>\n"
			"#include <R_ext/Memory.h>\n"
			"#ifndef Calloc\n"
			"#define Calloc(n, t) R_Calloc((n), t)\n"
			"#endif\n"
			"#ifndef Realloc\n"
			"#define Realloc(p, n, t) R_Realloc((p), (n), t)\n"
			"#endif\n"
			"#ifndef Free\n"
			"#define Free(p) R_Free(p)\n"
			"#endif\n"
		)

		files = [
			"src/classTree.c",
			"src/regTree.c",
			"src/rfutils.c",
			"src/regrf.c",
		]

		for relpath in files:
			# Prepend the compatibility block if it's not already present
			with open(relpath, "r", encoding="utf-8") as f:
				content = f.read()
			if "#define Calloc" not in content:
				with open(relpath, "w", encoding="utf-8") as f:
					f.write(insertion + content)
			else:
				# Fix previously-inserted incorrect macros to forward to R_* forms
				filter_file(
					r"^#define\s+Calloc\(n,\s*t\)\s*\(t\*\)\s*R_Calloc\(\(size_t\)\(n\),\s*sizeof\(t\)\)\s*$",
					r"#define Calloc(n, t) R_Calloc((n), t)",
					relpath,
					string=True,
				)
				filter_file(
					r"^#define\s+Realloc\(p,\s*n,\s*t\)\s*\(t\*\)\s*R_Realloc\(\(p\),\s*\(size_t\)\(n\),\s*sizeof\(t\)\)\s*$",
					r"#define Realloc(p, n, t) R_Realloc((p), (n), t)",
					relpath,
					string=True,
				)
				# Ensure RS.h include is present (needed for R_Calloc/R_Realloc)
				filter_file(
					r"(?m)^#include <R_ext/Memory.h>$",
					r"#include <R_ext/RS.h>\n#include <R_ext/Memory.h>",
					relpath,
					string=True,
				)
