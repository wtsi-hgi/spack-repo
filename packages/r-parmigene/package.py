# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParmigene(RPackage):
	"""Parallel Mutual Information Estimation for Gene Network
Reconstruction

	Parallel estimation of the mutual information based on entropy
    estimates from k-nearest neighbors distances and algorithms for the
    reconstruction of gene regulatory networks
    (Sales et al, 2011 <doi:10.1093/bioinformatics/btr274>).
	"""
	
	homepage = "https://github.com/sales-lab/parmigene"
	cran = "parmigene" 

	version("1.1.0", md5="b4e0213cf464ca63b6dc51f3133c975a")

	def setup_build_environment(self, env):
		"""Ensure compatibility with R >= 4.5 memory API.

		Older sources use Calloc/Realloc/Free without including the new
		memory headers. Force-include a tiny compatibility header that
		maps these macros to the modern API when building with R >= 4.5.
		"""
		if "r" in self.spec and self.spec["r"].satisfies("@4.5:"):
			compat_header = join_path(self.package_dir, "r45_compat.h")
			# Write the header next to the recipe for inclusion
			with open(compat_header, "w", encoding="utf-8") as f:
				f.write(
					"#ifndef R_PARMIGENE_R45_COMPAT_H\n"
					"#define R_PARMIGENE_R45_COMPAT_H\n"
					"#include <R.h>\n"
					"#include <R_ext/RS.h>\n"
					"#include <R_ext/Memory.h>\n"
					"#ifndef Calloc\n"
					"#define Calloc(n, T) (T*) R_Calloc((n), T)\n"
					"#endif\n"
					"#ifndef Realloc\n"
					"#define Realloc(p, n, T) (T*) R_Realloc((p), (n), T)\n"
					"#endif\n"
					"#ifndef Free\n"
					"#define Free(p) R_Free(p)\n"
					"#endif\n"
					"#endif /* R_PARMIGENE_R45_COMPAT_H */\n"
				)
			# Force-include the header during compilation
			env.append_flags("PKG_CPPFLAGS", f"-include {compat_header}")
