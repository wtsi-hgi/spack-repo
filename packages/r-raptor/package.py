# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaptor(RPackage):
	"""Row and Position Tracheid Organizer

	Performs wood cell anatomical data analyses on spatially explicit xylem (tracheids) datasets 
                  derived from thin sections of woody tissue. The package includes functions for visualisation, 
                  detection and alignment of continuous tracheid radial file (defined as rows) and individual tracheid position 
                  within an annual ring of coniferous species. This package is designed to be used with elaborate cell output, 
                  e.g. as provided with ROXAS (von Arx & Carrer, 2014 <doi:10.1016/j.dendro.2013.12.001>). The package has been validated for Picea abies, 
                  Larix Siberica, Pinus cembra and Pinus sylvestris.
	"""
	
	homepage = "https://the-hull.github.io/raptor/"
	cran = "RAPTOR" 

	version("1.0.1", md5="5b37d4077e34a814e3b4f6d95d742341")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
