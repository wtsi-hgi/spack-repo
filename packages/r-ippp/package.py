# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIppp(RPackage):
	"""Inhomogeneous Poisson Point Processes

	Generates random numbers corresponding to the events on a Poisson point process with changing event rates. This includes the possibility to incorporate additional information such as the number of events occurring or the location of an already known event. It can also generate the probability density functions of specific events in the cases where additional information is available. Based on Hohmann (2019) <arXiv:1901.10754>.
	"""
	
	cran = "IPPP" 

	version("1.1", md5="653e68256a6a8781e295cc082f9e4607")

