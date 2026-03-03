# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnschart(RPackage):
	"""Sequential Normal Scores in Statistical Process Management

	The methods discussed in this package are new non-parametric methods
    based on sequential normal scores 'SNS' (Conover et al (2017)
    <doi:10.1080/07474946.2017.1360091>), designed for sequences of observations,
    usually time series data, which may occur singly or in batches,
    and may be univariate or multivariate. These methods are designed
    to detect changes in the process, which may occur as changes in location
    (mean or median), changes in scale (standard deviation, or variance), or
    other changes of interest in the distribution of the observations,
    over the time observed. They usually apply to large data sets,
    so computations need to be simple enough to be done in a reasonable
    time on a computer, and easily updated as each new observation
    (or batch of observations) becomes available. Some examples and more detail
    in 'SNS' is presented in the work by Conover et al (2019) <arXiv:1901.04443>.
	"""
	
	cran = "SNSchart" 

	version("1.4.0", md5="30ef5c571f8f8cac3ddca27ca91acbe5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
