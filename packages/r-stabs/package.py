# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStabs(RPackage):
	"""Stability Selection with Error Control

	Resampling procedures to assess the stability of selected variables
    with additional finite sample error control for high-dimensional variable
    selection procedures such as Lasso or boosting. Both, standard stability
    selection (Meinshausen & Buhlmann, 2010, <doi:10.1111/j.1467-9868.2010.00740.x>) 
    and complementary pairs stability selection with improved error bounds 
    (Shah & Samworth, 2013, <doi:10.1111/j.1467-9868.2011.01034.x>) are
    implemented. The package can be combined with arbitrary user specified
    variable selection approaches.
	"""
	
	homepage = "https://github.com/hofnerb/stabs"
	cran = "stabs" 

	version("0.6-4", md5="b05e82dca362b6442b1c2d2970252509")

	depends_on("r@2.14:", type=("build", "run"))
