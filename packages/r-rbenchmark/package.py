# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbenchmark(RPackage):
	"""Benchmarking routine for R

	rbenchmark is inspired by the Perl module Benchmark, and
        is intended to facilitate benchmarking of arbitrary R code. The
        library consists of just one function, benchmark, which is a
        simple wrapper around system.time.  Given a specification of
        the benchmarking process (counts of replications, evaluation
        environment) and an arbitrary number of expressions, benchmark
        evaluates each of the expressions in the specified environment,
        replicating the evaluation as many times as specified, and
        returning the results conveniently wrapped into a data frame.
	"""
	
	homepage = "http://rbenchmark.googlecode.com"
	cran = "rbenchmark" 

	version("1.0.0", md5="e8fe50e0eebc3330d1fbe1c54678bf9f")

