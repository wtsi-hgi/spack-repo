# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLphom(RPackage):
	"""Ecological Inference by Linear Programming under Homogeneity

	Provides a bunch of algorithms based on linear programming for estimating, under 
    the homogeneity hypothesis, RxC ecological contingency tables (or vote transition matrices) 
    using mainly aggregate data (from voting units). 
    References: 
    Pavía and Romero (2022) <doi:10.1177/00491241221092725>.
    Pavía (2023) <doi:10.1007/s43545-023-00658-y>.
    Pavía and Romero (2024) <doi:10.1093/jrsssa/qnae013>.
    Pavía (2024) A local convergent ecological inference algorithm for RxC tables.
    Pavía and Penadés (2024). A bottom-up approach for ecological inference.
    Romero, Pavía, Martín and Romero (2020) <doi:10.1080/02664763.2020.1804842>.
    Acknowledgements:
    The authors wish to thank Consellería de Educación, Universidades y Empleo, Generalitat Valenciana (grant AICO/2021/257) and Ministerio de Economía e Innovación (grant PID2021-128228NB-I00) for supporting this research.
	"""
	
	cran = "lphom" 

	version("0.3.5-4", md5="29ad1a14c93519e46fe2cd48992fd436")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
