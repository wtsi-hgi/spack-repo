# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGensvm(RPackage):
	"""A Generalized Multiclass Support Vector Machine

	The GenSVM classifier is a generalized multiclass support vector
	machine (SVM). This classifier aims to find decision boundaries that
	separate the classes with as wide a margin as possible. In GenSVM, the
	loss function is very flexible in the way that misclassifications are
	penalized.  This allows the user to tune the classifier to the dataset
	at hand and potentially obtain higher classification accuracy than
	alternative multiclass SVMs.  Moreover, this flexibility means that
	GenSVM has a number of other multiclass SVMs as special cases. One of
	the other advantages of GenSVM is that it is trained in the primal
	space, allowing the use of warm starts during optimization.  This
	means that for common tasks such as cross validation or repeated model
	fitting, GenSVM can be trained very quickly. Based on: G.J.J. van den
	Burg and P.J.F. Groenen (2018) <https://www.jmlr.org/papers/v17/14-526.html>.
	"""
	
	homepage = "https://github.com/GjjvdBurg/RGenSVM"
	cran = "gensvm" 

	version("0.1.7", md5="84a63525990f78aec68fd388f77148e7")

	depends_on("r@3:", type=("build", "run"))
