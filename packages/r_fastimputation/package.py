# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastimputation(RPackage):
	"""Learn from Training Data then Quickly Fill in Missing Data

	TrainFastImputation() uses training data to describe a
    multivariate normal distribution that the data approximates or
    can be transformed into approximating and stores this information
    as an object of class 'FastImputationPatterns'. FastImputation()
    function uses this 'FastImputationPatterns' object to impute (make
    a good guess at) missing data in a single line or a whole data frame
    of data.  This approximates the process used by 'Amelia'
    <https://gking.harvard.edu/amelia> but is much faster when
    filling in values for a single line of data.
	"""
	
	cran = "FastImputation" 

	version("2.2.1", md5="f9e75793cc52c2a80b718711f77ea0f5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
