# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnlearn(RPackage):
	"""Bayesian Network Structure Learning, Parameter Learning and
Inference

	Bayesian network structure learning, parameter learning and inference.
  This package implements constraint-based (PC, GS, IAMB, Inter-IAMB, Fast-IAMB, MMPC,
  Hiton-PC, HPC), pairwise (ARACNE and Chow-Liu), score-based (Hill-Climbing and Tabu
  Search) and hybrid (MMHC, RSMAX2, H2PC) structure learning algorithms for discrete,
  Gaussian and conditional Gaussian networks, along with many score functions and
  conditional independence tests.
  The Naive Bayes and the Tree-Augmented Naive Bayes (TAN) classifiers are also implemented.
  Some utility functions (model comparison and manipulation, random data generation, arc
  orientation testing, simple and advanced plots) are included, as well as support for
  parameter estimation (maximum likelihood and Bayesian) and inference, conditional
  probability queries, cross-validation, bootstrap and model averaging.
  Development snapshots with the latest bugfixes are available from <https://www.bnlearn.com/>.
	"""
	
	homepage = "https://www.bnlearn.com/"
	cran = "bnlearn" 

	version("4.9.3", md5="c236e2f684a3795ea860fc132db67eae")
	version("4.9.2", md5="9bb72beab67578e9190e50b135fd36ca")
	version("4.9.1", md5="635e44be0c40c2e924118674ef1e9ec6")

	# R 4.5 removed legacy Calloc/Free unless including R_ext/Memory.h
	# Ensure compatibility by injecting the required include and macros for 4.9.3.
	def patch(self):
		# Apply only to the version that needs it
		if not self.spec.satisfies("@4.9.3"):
			return
		# Inject R 4.5 memory API compatibility into central header
		filter_file(
			r'^#include <R_ext/Utils.h>$',
			'#include <R_ext/Utils.h>\n'
			'#include <R_ext/Memory.h>\n'
			'#ifndef Calloc\n'
			'#define Calloc(n, T) (T*) R_Calloc((n), T)\n'
			'#endif\n'
			'#ifndef Free\n'
			'#define Free R_Free\n'
			'#endif',
			'src/include/rcore.h',
		)

	depends_on("r@4.3:", type=("build", "run"))
