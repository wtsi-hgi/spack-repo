# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQgametheory(RPackage):
	"""Quantum Game Theory Simulator

	General purpose toolbox for simulating quantum versions of game theoretic models (Flitney and Abbott 2002) <arXiv:quant-ph/0208069>. Quantum (Nielsen and Chuang 2010, ISBN:978-1-107-00217-3) versions of models that have been handled are: Penny Flip Game (David A. Meyer 1998) <arXiv:quant-ph/9804010>, Prisoner's Dilemma (J. Orlin Grabbe 2005) <arXiv:quant-ph/0506219>, Two Person Duel (Flitney and Abbott 2004) <arXiv:quant-ph/0305058>, Battle of the Sexes (Nawaz and Toor 2004) <arXiv:quant-ph/0110096>, Hawk and Dove Game (Nawaz and Toor 2010) <arXiv:quant-ph/0108075>, Newcomb's Paradox (Piotrowski and Sladkowski 2002) <arXiv:quant-ph/0202074> and Monty Hall Problem (Flitney and Abbott 2002) <arXiv:quant-ph/0109035>.
	"""
	
	homepage = "https://github.com/indrag49/QGameTheory"
	cran = "QGameTheory" 

	version("0.1.2", md5="4e1dac48d946f0562f008e2d8221b463")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
