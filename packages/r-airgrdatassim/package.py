# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAirgrdatassim(RPackage):
	"""Ensemble-Based Data Assimilation with GR Hydrological Models

	Add-on to the 'airGR' package which provides the tools to assimilate observed discharges in daily GR hydrological models. The package consists in two functions allowing to perform the assimilation of observed discharges via the Ensemble Kalman filter or the Particle filter as described in Piazzi et al. (2021) <doi:10.1029/2020WR028390>.
	"""
	
	cran = "airGRdatassim" 

	version("0.1.3", md5="5f7995b9c76483303d0951c30808bac3")

	depends_on("r-airgr@1.6.9.27:", type=("build", "run"))
