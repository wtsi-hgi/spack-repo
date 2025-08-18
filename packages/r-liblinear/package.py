# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiblinear(RPackage):
	"""Linear Predictive Models Based on the LIBLINEAR C/C++ Library

	A wrapper around the LIBLINEAR C/C++ library for machine
        learning (available at
        <https://www.csie.ntu.edu.tw/~cjlin/liblinear/>). LIBLINEAR is
        a simple library for solving large-scale regularized linear
        classification and regression. It currently supports
        L2-regularized classification (such as logistic regression,
        L2-loss linear SVM and L1-loss linear SVM) as well as
        L1-regularized classification (such as L2-loss linear SVM and
        logistic regression) and L2-regularized support vector
        regression (with L1- or L2-loss). The main features of
        LiblineaR include multi-class classification (one-vs-the rest,
        and Crammer & Singer method), cross validation for model
        selection, probability estimates (logistic regression only) or
        weights for unbalanced data. The estimation of the models is
        particularly fast as compared to other libraries.
	"""
	
	homepage = "<https://dnalytics.com/software/liblinear/>"
	cran = "LiblineaR" 

	version("2.10-23", md5="d273f6ac41fba1e7a32e3938f26c433d")


	def patch(self):
		# R >=4.5: Calloc/Realloc/Free moved behind R_ext/Memory.h
		# Ensure the header is included in all native sources.
		for source_path in [
			"src/predictLinear.c",
			"src/trainLinear.c",
			"src/linear.cpp",
		]:
			# First, try to insert after an exact '#include <R.h>'
			filter_file(
				"#include <R.h>",
				"#include <R.h>\n#include <R_ext/Memory.h>",
				source_path,
			)
			# If that did not hit (e.g., uses quotes or different include order),
			# prepend the include at the top as a fallback.
			filter_file(
				r"^(.*)$",
				"#include <R_ext/Memory.h>\n\\1",
				source_path,
				string=True,
			)
			# Ensure fallbacks if Calloc/Free/Realloc still undefined under R >= 4.5
			filter_file(
				r"^#include <R_ext/Memory.h>$",
				"#include <R_ext/Memory.h>\n#ifndef Calloc\n#define Calloc(n,t) R_Calloc((n), t)\n#endif\n#ifndef Realloc\n#define Realloc(p,n,t) R_Realloc((p),(n), t)\n#endif\n#ifndef Free\n#define Free(p) R_Free((p))\n#endif",
				source_path,
			)
			# Fix any previously injected incorrect macro definitions
			filter_file(r"#define Calloc\(n,t\) \(t\*\) R_Calloc\(\(n\), sizeof\(t\)\)", "#define Calloc(n,t) R_Calloc((n), t)", source_path)
			filter_file(r"#define Realloc\(p,n,t\) \(t\*\) R_Realloc\(\(p\),\(n\), sizeof\(t\)\)", "#define Realloc(p,n,t) R_Realloc((p),(n), t)", source_path)

