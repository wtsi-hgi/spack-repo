# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThermimage(RPackage):
	"""Thermal Image Analysis

	A collection of functions and routines for inputting thermal
    image video files, plotting and converting binary raw data into estimates of
    temperature.  First published 2015-03-26.  Written primarily for research purposes
    in biological applications of thermal images.  v1 included the base calculations 
    for converting thermal image binary values to temperatures. v2 included additional
    equations for providing heat transfer calculations and an import function for thermal
    image files (v2.2.3 fixed error importing thermal image to windows OS). v3. Added numerous
    functions for converting thermal image, videos, rewriting and exporting.  
    v3.1. Added new functions to convert files. v3.2.  Fixed the various functions related to finding frame times.
    v4.0. fixed an error in atmospheric attenuation constants, affecting raw2temp and temp2raw functions.
    Recommend update for use with long distance calculations. v.4.1.3 changed to frameLocates to reflect change to as.character() to format().
	"""
	
	homepage = "https://cran.r-project.org/package=Thermimage"
	cran = "Thermimage" 

	version("4.1.3", md5="42cb8678fd36a82538b8ae712679e491")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("perl", type=("build", "link", "run"))
	depends_on("ffmpeg", type=("build", "link", "run"))
	depends_on("imagemagick", type=("build", "link", "run"))
