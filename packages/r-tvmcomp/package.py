# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTvmcomp(RPackage):
	"""Discounting and Compounding Calculations for Various Scenarios

	Functions for compounding and discounting calculations included here serve as a complete reference for various scenarios of time value of money.
    Raymond M. Brooks (“Financial Management,” 2018, ISBN: 9780134730417).
    Sheridan Titman, Arthur J. Keown, John D. Martin (“Financial Management: Principles and Applications,” 2017, ISBN: 9780134417219).
    Jonathan Berk, Peter DeMarzo, David Stangeland, Andras Marosi (“Fundamentals of Corporate Finance,” 2019, ISBN: 9780134735313).
    S. A. Hummelbrunner, Kelly Halliday, Ali R. Hassanlou (“Contemporary Business Mathematics with Canadian Applications,” 2020, ISBN: 9780135285015).
	"""
	
	cran = "tvmComp" 

	version("1.0.2", md5="4424567e723c17b7c1065c9da3c9df91")

	depends_on("r-rdpack", type=("build", "run"))
