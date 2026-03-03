# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcbackscattering(RPackage):
	"""Monte Carlo Simulation for Surface Backscattering

	Monte Carlo simulation is a stochastic method computing trajectories of photons in media. Surface backscattering is performing calculations in semi-infinite media and summarizing photon flux leaving the surface. This simulation is modeling the optical measurement of diffuse reflectance using an incident light beam. The semi-infinite media is considered to have flat surface. Media, typically biological tissue, is described by four optical parameters: absorption coefficient, scattering coefficient, anisotropy factor, refractive index. The media is assumed to be homogeneous.
    Computational parameters of the simulation include: number of photons, radius of incident light beam, lowest photon energy threshold, intensity profile (halo) radius, spatial resolution of intensity profile.
    You can find more information and validation in the Open Access paper.
    Laszlo Baranyai (2020) <doi:10.1016/j.mex.2020.100958>.
	"""
	
	cran = "MCBackscattering" 

	version("0.1.1", md5="e1bc8772d84ff7d049e2146999b592bd")

