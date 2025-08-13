# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class RSpatialreg(RPackage):
	"""Spatial Regression Analysis.

	A collection of all the estimation functions for spatial cross-sectional
	models (on lattice/areal data using spatial weights matrices) contained up
	to now in 'spdep', 'sphet' and 'spse'. These model fitting functions
	include maximum likelihood methods for cross-sectional models proposed by
	'Cliff' and 'Ord' (1973, ISBN:0850860369) and (1981, ISBN:0850860814),
	fitting methods initially described by 'Ord' (1975)
	<doi:10.1080/01621459.1975.10480272>. The models are further described by
	'Anselin' (1988) <doi:10.1007/978-94-015-7799-1>. Spatial two stage least
	squares and spatial general method of moment models initially proposed by
	'Kelejian' and 'Prucha' (1998) <doi:10.1023/A:1007707430416> and (1999)
	<doi:10.1111/1468-2354.00027> are provided. Impact methods and MCMC fitting
	methods proposed by 'LeSage' and 'Pace' (2009) <doi:10.1201/9781420064254>
	are implemented for the family of cross-sectional spatial regression
	models. Methods for fitting the log determinant term in maximum likelihood
	and MCMC fitting are compared by 'Bivand et al.' (2013)
	<doi:10.1111/gean.12008>, and model fitting methods by 'Bivand' and 'Piras'
	(2015) <doi:10.18637/jss.v063.i18>; both of these articles include
	extensive lists of references. 'spatialreg' >= 1.1-* correspond to 'spdep'
	>= 1.1-1, in which the model fitting functions are deprecated and pass
	through to 'spatialreg', but will mask those in 'spatialreg'. From versions
	1.2-*, the functions will be made defunct in 'spdep'."""

	cran = "spatialreg"
	version("1.3-2", md5="c832754d3d9a3bd5315204b2e6052683")
	version("1.2-8", sha256="150cb77ca09800d93af7de37440072d59ac7e41acb45ab42fc1c0e59edd7f9de")
	version("1.2-6", sha256="9b384117a31ab5fe830325b3eacbec5eb9d40bf0e9ca3c75ea15ca6b78fbd41d")
	version("1.2-3", sha256="09e0e65f043975d5c1d4be99ef9f29cf0790e962dcde9b7e45a7027d268fce22")
	version("1.2-1", sha256="4c40b6b331aa8818254633cfb80d4b9a03b2b6fac2c0104b3b99201d447ba081")
	version("1.1-5", sha256="ddbf0773bad2e99b306116ae99a57bf29eecf723d1735820935a6fb7f331b27d")
	version("1.1-3", sha256="7609cdfcdfe427d2643a0db6b5360be3f6d60ede8229436ab52092d1c9cf0480")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-spdata", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spdep@1.3.1:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-learnbayes", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))

	# R 4.4+ requires explicitly including R_ext/Memory.h for Calloc/Free macros.
	# spatialreg 1.3-2 uses Calloc/Free with a type argument (macro form).
	# Ensure headers are included to avoid compile errors against newer R.
	def patch(self):
		if self.spec.satisfies("@1.3-2"):
			src_dir = join_path(self.stage.source_path, "src")
			if os.path.isdir(src_dir):
				for filename in os.listdir(src_dir):
					if not filename.endswith(".c"):
						continue
					path = join_path(src_dir, filename)
					# Insert Memory.h after R.h includes when present
					# Ensure Memory.h is included with a real newline after R.h
					filter_file(
						# Match either <R.h> or "R.h"
						 r"(#include\s+[<\"]R.h[>\"])",
						 "\\1\n#include <R_ext/Memory.h>",
						 path,
					)
					# Fix any accidental literal "\n" sequences from prior edits
					filter_file(
						 r"(<R.h>)\\n#include <R_ext/Memory.h>",
						 "\\1\n#include <R_ext/Memory.h>",
						 path,
					)
				# Also ensure the package header includes Memory.h, as sources include it
				header_path = join_path(src_dir, "spatialreg.h")
				if os.path.exists(header_path):
					# Prepend RS.h/Memory.h early to ensure Calloc/Free macros
					filter_file(
						 r"(^#ifndef USE_FC_LEN_T)",
						 "#include <R_ext/RS.h>\n#include <R_ext/Memory.h>\n\\1",
						 header_path,
					)
					# Fix any accidental literal "\n" sequences from prior edits
					filter_file(
						 r"#include <R_ext/RS.h>\\n#include <R_ext/Memory.h>\\n#ifndef",
						 "#include <R_ext/RS.h>\n#include <R_ext/Memory.h>\n#ifndef",
						 header_path,
					)
					# Map legacy Calloc/Free macros to modern R_Calloc/R_Free
					filter_file(
						 r"(#include\s+<R_ext/Memory.h>)",
						 "\\1\n#ifndef Calloc\n#define Calloc(n,t) R_Calloc(n,t)\n#endif\n#ifndef Free\n#define Free(p) R_Free(p)\n#endif",
						 header_path,
					)
