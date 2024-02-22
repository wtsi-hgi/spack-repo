# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoughsets(RPackage):
	"""Data Analysis Using Rough Set and Fuzzy Rough Set Theories

	Implementations of algorithms for data analysis based on the
    rough set theory (RST) and the fuzzy rough set theory (FRST). We not only
    provide implementations for the basic concepts of RST and FRST but also
    popular algorithms that derive from those theories. The methods included in the
    package can be divided into several categories based on their functionality:
    discretization, feature selection, instance selection, rule induction and
    classification based on nearest neighbors. RST was introduced by Zdzisław
    Pawlak in 1982 as a sophisticated mathematical tool to model and process
    imprecise or incomplete information. By using the indiscernibility relation for
    objects/instances, RST does not require additional parameters to analyze the
    data. FRST is an extension of RST. The FRST combines concepts of vagueness and
    indiscernibility that are expressed with fuzzy sets (as proposed by Zadeh, in
    1965) and RST.
	"""
	
	homepage = "https://github.com/janusza/RoughSets"
	cran = "RoughSets" 

	version("1.3-8", md5="88ced311d1bac056d2bf83b2508931bf")

	depends_on("r-rcpp", type=("build", "run"))
