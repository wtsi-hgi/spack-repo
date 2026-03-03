# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowerpkg(RPackage):
	"""Power Analyses for the Affected Sib Pair and the TDT Design

	There are two main functions: (1) To estimate the power of testing for linkage using an
        affected sib pair design, as a function of the recurrence risk
        ratios. We will use analytical power formulae as implemented in
        R. These are based on a Mathematica notebook created by Martin
        Farrall. (2) To examine how the power of the transmission
        disequilibrium test (TDT) depends on the disease allele
        frequency, the marker allele frequency, the strength of the
        linkage disequilibrium, and the magnitude of the genetic
        effect. We will use an R program that implements the power
        formulae of Abel and Muller-Myhsok (1998). These formulae allow
        one to quickly compute power of the TDT approach under a
        variety of different conditions. This R program was modeled on
        Martin Farrall's Mathematica notebook.
	"""
	
	cran = "powerpkg" 

	version("1.6", md5="b070d189b3aaf1ea9cc078932a6c2e17")

