# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class RCoxme(RPackage):
	"""Mixed Effects Cox Models

	Fit Cox proportional hazards models containing both 
 fixed and random effects.  The random effects can have a general form, of which
 familial interactions (a "kinship" matrix) is a particular special case. 
 Note that the simplest case of a mixed effects Cox model, i.e. a single random 
 per-group intercept, is also called a "frailty" model.  The approach is based
 on Ripatti and Palmgren, Biometrics 2002.
	"""
	
	cran = "coxme" 

	version("2.2-20", md5="abdedf5f369bb583ee224f654fec8323")
	version("2.2-18.1", md5="6f86a36d721b09094a926ceea3dba301")

	depends_on("r-survival@2.36.14:", type=("build", "run"))
	depends_on("r-bdsmatrix", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-matrix@1:", type=("build", "run"))

	# R >= 4.4 tightened memory API; ensure legacy Calloc/Free compile
	def patch(self):
		src_dir = join_path(self.stage.source_path, "src")
		if os.path.isdir(src_dir):
			for filename in os.listdir(src_dir):
				if not filename.endswith(".c"):
					continue
				path = join_path(src_dir, filename)
				# Ensure Memory.h is available after R.h
				filter_file(
					r"(#include\s+[<\"]R.h[>\"])",
					"\\1\n#include <R_ext/Memory.h>",
					path,
				)
				# Provide Calloc/Free macros if missing
				filter_file(
					r"(#include\s+<R_ext/Memory.h>)",
					"\\1\n#ifndef Calloc\n#define Calloc(n, T) (T*) R_Calloc((n), T)\n#endif\n#ifndef Free\n#define Free(p) R_Free(p)\n#endif",
					path,
				)
				# If R.h is not directly included in this file, inject after bdsmatrix.h
				filter_file(
					r"(#include\s+[<\"]bdsmatrix.h[>\"])",
					"\\1\n#include <R.h>\n#include <R_ext/Memory.h>\n#ifndef Calloc\n#define Calloc(n, T) (T*) R_Calloc((n), T)\n#endif\n#ifndef Free\n#define Free(p) R_Free(p)\n#endif",
					path,
				)
