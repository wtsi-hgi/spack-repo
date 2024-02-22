# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROcc(RPackage):
	"""Estimates PET Neuroreceptor Occupancies

	Generic function for estimating positron emission tomography (PET) neuroreceptor occupancies from the total volumes of distribution of a set of regions of interest. Fittings methods include the simple 'reference region' and 'ordinary least squares' (sometimes known as occupancy plot) methods, as well as the more efficient 'restricted maximum likelihood estimation'.
	"""
	
	cran = "occ" 

	version("1.1", md5="136772f909dbd4275dd737a725b3f385")

