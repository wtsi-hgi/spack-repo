# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatstatExplore(RPackage):
	"""Exploratory Data Analysis for the 'spatstat' Family.

	Functionality for exploratory data analysis and nonparametric analysis of
	spatial data, mainly spatial point patterns, in the 'spatstat' family of
	packages. (Excludes analysis of spatial data on a linear network, which is
	covered by the separate package 'spatstat.linnet'.) Methods include quadrat
	counts, K-functions and their simulation envelopes, nearest neighbour
	distance and empty space statistics, Fry plots, pair correlation function,
	kernel smoothed intensity, relative risk estimation with cross-validated
	bandwidth selection, mark correlation functions, segregation indices, mark
	dependence diagnostics, and kernel estimates of covariate effects. Formal
	hypothesis tests of random pattern (chi-squared, Kolmogorov-Smirnov, Monte
	Carlo, Diggle-Cressie-Loosmore-Ford, Dao-Genton, two-stage Monte Carlo) and
	tests for covariate effects (Cox-Berman-Waller-Lawson, Kolmogorov-Smirnov,
	ANOVA) are also supported."""

	cran = "spatstat.explore"
	version("3.2-7", md5="59cd51e92feabafdee60c40062878a43")
	version("3.2-6", md5="49ee5844d94a714c9bbeb3110ba1ce9e")
	version("3.1-0", sha256="87ef4882652db3b834214bfc776dd7d23d931a9227de12f19722aeb1029d086e")
	version("3.0-3", sha256="137444a46d26d88241336feece63ed7b006a9328cfe3861d4b8ab7b4bed963a7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spatstat-data@3.0.4:", type=("build", "run"))
	depends_on("r-spatstat-geom@3.2.9:", type=("build", "run"))
	depends_on("r-spatstat-random@3.2.3:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-spatstat-utils@3.0.4:", type=("build", "run"))
	depends_on("r-spatstat-sparse@3.0.3:", type=("build", "run"))
	depends_on("r-goftest@1.2-2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))

	def setup_build_environment(self, env):
		# Some C files use PI constant directly
		env.append_flags("CPPFLAGS", "-DPI=3.14159265358979323846")

	def patch(self):
		# Ensure PI is defined in C sources where used
		import os
		c_path = os.path.join('src', 'sphevol.c')
		if os.path.exists(c_path):
			with open(c_path, 'r', encoding='utf-8') as f:
				content = f.read()
			injection = (
				"\n#ifndef PI\n"
				"#define PI 3.14159265358979323846\n"
				"#endif\n"
			)
			if 'PI 3.14159265358979323846' not in content:
				parts = content.split('\n')
				insert_idx = 0
				for idx, line in enumerate(parts[:50]):
					if line.startswith('#include'):
						insert_idx = idx + 1
					else:
						if insert_idx and not line.startswith('#include'):
							break
				new_content = '\n'.join(parts[:insert_idx]) + injection + '\n'.join(parts[insert_idx:])
				with open(c_path, 'w', encoding='utf-8') as f:
					f.write(new_content)
