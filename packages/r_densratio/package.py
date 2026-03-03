# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDensratio(RPackage):
	"""Density Ratio Estimation

	Density ratio estimation.
    The estimated density ratio function can be used in many applications such as
    anomaly detection, change-point detection, covariate shift adaptation.
    The implemented methods are uLSIF (Hido et al. (2011) <doi:10.1007/s10115-010-0283-2>),
    RuLSIF (Yamada et al. (2011) <doi:10.1162/NECO_a_00442>),
    and KLIEP (Sugiyama et al. (2007) <doi:10.1007/s10463-008-0197-x>).
	"""
	
	homepage = "https://github.com/hoxo-m/densratio"
	cran = "densratio" 

	version("0.2.1", md5="bd9dbf12d23fa35dcce6093ae3174864")

