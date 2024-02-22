# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFpcb(RPackage):
	"""Predictive Confidence Bands for Functional Time Series
Forecasting

	Functions to represent functional objects under a Reproducing Kernel Hilbert Space (RKHS) framework as described 
  in Muñoz & González (2010). Autoregressive Hilbertian Model for functional time series using RKHS and predictive confidence bands construction 
  as proposed in Hernández et al (2021).
	"""
	
	cran = "fpcb" 

	version("0.1.0", md5="1637c87a0406bb0a35e79ea6f48e1ffd")

	depends_on("r-fnn", type=("build", "run"))
