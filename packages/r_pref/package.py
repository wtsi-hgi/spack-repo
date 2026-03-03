# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPref(RPackage):
	"""Preference Voting with Explanatory Graphics

	Implements the Single Transferable Vote (STV) electoral system, with
    clear explanatory graphics. The core function stv() uses Meek's method, the purest
    expression of the simple principles of STV, but which requires electronic
    counting. It can handle votes expressing equal preferences for subsets of
    the candidates. A function stv.wig() implementing the Weighted Inclusive
    Gregory method, as used in Scottish council elections, is also provided,
    and with the same options, as described in the manual. The required vote
    data format is as an R list: a function pref.data() is provided to transform
    some commonly used data formats into this format.
    References for methodology:
    Hill, Wichmann and Woodall (1987) <doi:10.1093/comjnl/30.3.277>,
    Hill, David (2006) <https://www.votingmatters.org.uk/ISSUE22/I22P2.pdf>,
    Mollison, Denis (2023) <arXiv:2303.15310>,
    (see also the package manual pref_pkg_manual.pdf).
	"""
	
	homepage = "https://github.com/denismollison/pref"
	cran = "pref" 

	version("0.4.0", md5="935695cac5cc3c4cced6c956c7092060")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
