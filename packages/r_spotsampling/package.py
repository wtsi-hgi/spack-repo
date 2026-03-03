# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpotsampling(RPackage):
	"""SPatial and Optimally Temporal (SPOT) Sampling

	In spatial data, information of two neighboring units are generally very similar. 
  For spatial sampling, it is therefore more efficient to select samples that are well spread out in space. Often, the interest lies not only in estimating a measure at one point in time, but rather in estimating several points in time to also study the evolution. 
  Three new methods called Orfs (Optimal Rotation with Fixed sample Size), Orsp (Optimal Rotation with Spread sample), and Spot (Spatial and Optimally Temporal Sampling) are implemented in this package. Orfs allows to select temporal samples with fixed size. Orsp selects spatio-temporal samples with random size that are well spread out in space at each point in time. And Spot generates spread sample with fixed sample size at each wave. These methods provide an optimal time rotation of the selected units using the systematic sampling.
	"""
	
	cran = "SpotSampling" 

	version("0.1.0", md5="382c953f53278937e08a6ca8117d1304")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-balancedsampling", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-wavesampling", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
