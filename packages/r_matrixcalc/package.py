# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixcalc(RPackage):
	"""Collection of Functions for Matrix Calculations

	A collection of functions to support matrix calculations
        for probability, econometric and numerical analysis. There are
        additional functions that are comparable to APL functions which
        are useful for actuarial models such as pension mathematics.
        This package is used for teaching and research purposes at the
        Department of Finance and Risk Engineering, New York
        University, Polytechnic Institute, Brooklyn, NY 11201.
        Horn, R.A. (1990) Matrix Analysis. ISBN 978-0521386326.
        Lancaster, P. (1969) Theory of Matrices. ISBN 978-0124355507.
        Lay, D.C. (1995) Linear Algebra: And Its Applications. ISBN 978-0201845563.
	"""
	
	cran = "matrixcalc" 

	version("1.0-6", md5="3b7acd84cfbe8085fab05d2f40ff0c79")

	depends_on("r@2.0.1:", type=("build", "run"))
