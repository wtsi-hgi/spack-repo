# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBain(RPackage):
	"""Bayes Factors for Informative Hypotheses

	Computes approximated adjusted fractional Bayes factors for
    equality, inequality, and about equality constrained hypotheses.
    For a tutorial on this method, see Hoijtink, Mulder, van Lissa, & Gu,
    (2019) <doi:10.31234/osf.io/v3shc>. For applications in structural equation
    modeling, see: Van Lissa, Gu, Mulder, Rosseel, Van Zundert, &
    Hoijtink, (2021) <doi:10.1080/10705511.2020.1745644>. For the statistical
    underpinnings, see Gu, Mulder, and Hoijtink (2018) <doi:10.1111/bmsp.12110>;
    Hoijtink, Gu, & Mulder, J. (2019) <doi:10.1111/bmsp.12145>; Hoijtink, Gu, 
    Mulder, & Rosseel, (2019) <doi:10.31234/osf.io/q6h5w>.
	"""
	
	homepage = "https://informative-hypotheses.sites.uu.nl/software/bain/"
	cran = "bain" 

	version("0.2.10", md5="2402d81601918aa2204aa4cd2bb7aa1c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
