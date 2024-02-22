# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKitagawa(RPackage):
	"""Spectral Response of Water Wells to Harmonic Strain and Pressure
Signals

	Provides tools to calculate the theoretical hydrodynamic response
    of an aquifer undergoing harmonic straining or pressurization, or analyze
    measured responses. There are
    two classes of models here, designed for use with confined
    aquifers: (1) for sealed wells, based on the model of 
    Kitagawa et al (2011, <doi:10.1029/2010JB007794>), 
    and (2) for open wells, based on the models of
    Cooper et al (1965, <doi:10.1029/JZ070i016p03915>), 
    Hsieh et al (1987, <doi:10.1029/WR023i010p01824>), 
    Rojstaczer (1988, <doi:10.1029/JB093iB11p13619>), 
    Liu et al (1989, <doi:10.1029/JB094iB07p09453>), and
    Wang et al (2018, <doi:10.1029/2018WR022793>). Wang's 
    solution is a special exception which
    allows for leakage out of the aquifer 
    (semi-confined); it is equivalent to Hsieh's model
    when there is no leakage (the confined case).
    These models treat strain (or aquifer head) as an input to the
    physical system, and fluid-pressure (or water height) as the output. The
    applicable frequency band of these models is characteristic of seismic
    waves, atmospheric pressure fluctuations, and solid earth tides.
	"""
	
	homepage = "https://github.com/abarbour/kitagawa"
	cran = "kitagawa" 

	version("3.1.2", md5="7f7a33f6df006b70d6787326fe59eb00")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-bessel", type=("build", "run"))
	depends_on("r-kelvin@1.2:", type=("build", "run"))
	depends_on("r-psd@2:", type=("build", "run"))
