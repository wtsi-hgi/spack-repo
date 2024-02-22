# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFishresp(RPackage):
	"""Analytical Tool for Aquatic Respirometry

	Calculates metabolic rate of fish and other aquatic organisms measured using
             an intermittent-flow respirometry approach. The tool is used to run a set of graphical
             QC tests of raw respirometry data, correct it for background respiration and chamber
             effect, filter and extract target values of absolute and mass-specific metabolic rate.
             Experimental design should include background respiration tests and measuring of one
             or more metabolic rate traits. The R package is ideally integrated with the pump
             controller 'PumpResp' and the DO meter 'SensResp' (open-source hardware by FishResp).
             Raw respirometry data can be also imported from 'AquaResp' (free software), 'AutoResp'
             ('LoligoSystems'), 'OxyView' ('PreSens'), 'Pyro Oxygen Logger' ('PyroScience') and
             'Q-box Aqua' ('QubitSystems'). More information about the R package 'FishResp'is
             available in the publication by Morozov et al. (2019) <doi:10.1093/conphys/coz003>.
	"""
	
	homepage = "https://fishresp.org"
	cran = "FishResp" 

	version("1.1.1", md5="8eacb0d1df032455663e6b2f6a10c4a1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-rmr", type=("build", "run"))
	depends_on("r-respirometry", type=("build", "run"))
