# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFixseqmtp(RPackage):
	"""Fixed Sequence Multiple Testing Procedures

	Several generalized / directional Fixed Sequence Multiple Testing
    Procedures (FSMTPs) are developed for testing a sequence of pre-ordered
    hypotheses while controlling the FWER, FDR and Directional Error (mdFWER).
    All three FWER controlling generalized FSMTPs are designed under arbitrary
    dependence, which allow any number of acceptances. Two FDR controlling
    generalized FSMTPs are respectively designed under arbitrary dependence and
    independence, which allow more but a given number of acceptances. Two mdFWER
    controlling directional FSMTPs are respectively designed under arbitrary
    dependence and independence, which can also make directional decisions based
    on the signs of the test statistics. The main functions for each proposed
    generalized / directional FSMTPs are designed to calculate adjusted p-values
    and critical values, respectively. For users' convenience, the functions also
    provide the output option for printing decision rules.
	"""
	
	cran = "FixSeqMTP" 

	version("0.1.2", md5="7f98f66bfd0ffd75bf6a629bc9ba0e8f")

