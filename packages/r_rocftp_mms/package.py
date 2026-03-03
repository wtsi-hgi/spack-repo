# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRocftpMms(RPackage):
	"""Perfect Sampling

	The algorithm provided in this package generates perfect sample for unimodal or multimodal posteriors. Read Once Coupling From The Past, with Metropolis-Multishift is used to generate a perfect sample for a given posterior density based on the two extreme starting paths, minimum and maximum of the most interest range of the posterior. It uses the monotone random operation of multishift coupler which allows to sandwich all of the state space in one point. It means both Markov Chains starting from the maximum and minimum will be coalesced. The generated sample is independent from the starting points. It is useful for mixture distributions too. The output of this function is a real value as an exact draw from the posterior distribution.
	"""
	
	homepage = "https://github.com/nabipoor/ROCFTP.MMS"
	cran = "ROCFTP.MMS" 

	version("1.0.0", md5="7196e5814ebe4f4bb009296f32a9fcdc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-vctrs@0.3.8:", type=("build", "run"))
