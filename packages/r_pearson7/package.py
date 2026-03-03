# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPearson7(RPackage):
	"""Maximum Likelihood Inference for the Pearson VII Distribution
with Shape Parameter 3/2

	Supports maximum likelihood inference for the Pearson VII
    distribution with shape parameter 3/2 and free location and scale
    parameters. This distribution is relevant when estimating the velocity of
    processive motor proteins with random detachment.
	"""
	
	cran = "pearson7" 

	version("1.0-3", md5="953962e672e07a14a8484295375c949e", url="https://cran.r-project.org/src/contrib/pearson7_1.0-3.tar.gz")

