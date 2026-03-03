# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsospecr(RPackage):
	"""The IsoSpec Algorithm

	IsoSpec is a fine structure calculator used for obtaining the most
    probable masses of a chemical compound given the frequencies of the composing
    isotopes and their masses. It finds the smallest set of isotopologues with
    a given probability. The probability is assumed to be that of the product of
    multinomial distributions, each corresponding to one particular element and
    parametrized by the frequencies of finding these elements in nature. These
    numbers are supplied by IUPAC - the International Union of Pure and Applied
    Chemistry. See: Lacki, Valkenborg, Startek (2020) <DOI:10.1021/acs.analchem.0c00959>
    and Lacki, Startek, Valkenborg, Gambin (2017) <DOI:10.1021/acs.analchem.6b01459>
    for the description of the algorithms used.
	"""
	
	homepage = "http://matteolacki.github.io/IsoSpec/"
	cran = "IsoSpecR" 

	version("2.1.3", md5="5fc1153bfc9a320b70105eb04ed3bdc4")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
