# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemokde(RPackage):
	"""Kernel Density Estimation for Demonstration Purposes

	Demonstration code showing how (univariate) kernel
	     density estimates are computed, at least conceptually,
	     and allowing users to experiment with different kernels,
	     should they so wish.  The method used follows directly
	     the definition, but gains efficiency by replacing the
	     observations by frequencies in a very fine grid covering
	     the sample range.  A canonical reference is
	     B. W. Silverman, (1998) <doi: 10.1201/9781315140919>.
	     NOTE: the density function in the
	     stats package uses a more sophisticated method based on the
	     fast Fourier transform and that function should be used if
	     computational efficiency is a prime consideration.
	"""
	
	cran = "demoKde" 

	version("1.0.1", md5="e2e8b55e6388294032d3891b22682fdd")

