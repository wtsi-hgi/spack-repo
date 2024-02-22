# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRetrodesign(RPackage):
	"""Tools for Type S (Sign) and Type M (Magnitude) Errors

	Provides tools for working with Type S (Sign) and
    Type M (Magnitude) errors, as proposed in Gelman and Tuerlinckx (2000)
    <doi:10.1007/s001800000040> and
    Gelman & Carlin (2014) <doi:10.1177/1745691614551642>.
    In addition to simply calculating the probability of
    Type S/M error, the package includes functions for calculating these errors
    across a variety of effect sizes for comparison, and recommended sample size
    given "tolerances" for Type S/M errors. To improve the speed of these
    calculations, closed forms solutions for the probability of a Type S/M error
    from Lu, Qiu, and Deng (2018) <doi:10.1111/bmsp.12132>
    are implemented. As of 1.0.0, this includes
    support only for simple research designs. See the
    package vignette for a fuller exposition on how Type S/M errors arise in
    research, and how to analyze them using the type of design analysis proposed
    in the above papers.
	"""
	
	homepage = "https://github.com/andytimm/retrodesign"
	cran = "retrodesign" 

	version("0.2.1", md5="a109b4ff26b6657cc979629e13e0f552")

	depends_on("r@3.1:", type=("build", "run"))
