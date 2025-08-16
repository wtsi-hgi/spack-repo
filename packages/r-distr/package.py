# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class RDistr(RPackage):
	"""Object Oriented Implementation of Distributions

	S4-classes and methods for distributions.
	"""
	
	homepage = "http://distr.r-forge.r-project.org/"
	cran = "distr" 

	version("2.9.3", md5="516d41cdd753fb0a200d0122332ed9b8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-startupmsg", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

	# R 4.4+ removed legacy Calloc/Free unless Memory.h is included.
	# Ensure compatibility by including Memory.h and mapping legacy macros.
	def patch(self):
		# Only needed for newer R toolchains
		src_dir = join_path(self.stage.source_path, "src")
		if os.path.isdir(src_dir):
			for filename in os.listdir(src_dir):
				if not filename.endswith(".c"):
					continue
				path = join_path(src_dir, filename)
				# Ensure R_ext/Memory.h is included after R.h to provide R_Calloc/R_Free
				filter_file(
					r"(#include\s+[<\"]R.h[>\"])",
					"\\1\n#include <R_ext/Memory.h>",
					path,
				)
				# Map legacy Calloc/Free(n, T) to modern R_Calloc/R_Free if not defined
				filter_file(
					r"(#include\s+<R_ext/Memory.h>)",
					"\\1\n#ifndef Calloc\n#define Calloc(n, T) (T*) R_Calloc((n), T)\n#endif\n#ifndef Free\n#define Free(p) R_Free(p)\n#endif",
					path,
				)
