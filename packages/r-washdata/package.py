# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWashdata(RPackage):
	"""Urban Water and Sanitation Survey Dataset

	Urban water and sanitation survey dataset collected by Water and
    Sanitation for the Urban Poor (WSUP) with technical support from 
    Valid International. These citywide surveys have been collecting data 
    allowing water and sanitation service levels across the entire city to be 
    characterised, while also allowing more detailed data to be collected in 
    areas of the city of particular interest. These surveys are intended to 
    generate useful information for others working in the water and sanitation
    sector. Current release version includes datasets collected from a survey 
    conducted in Dhaka, Bangladesh in March 2017. This survey in Dhaka is one of 
    a series of surveys to be conducted by WSUP in various
    cities in which they operate including Accra, Ghana; Nakuru, Kenya; 
    Antananarivo, Madagascar; Maputo, Mozambique; and, Lusaka, Zambia. This 
    package will be updated once the surveys in other cities are completed and 
    datasets have been made available.
	"""
	
	homepage = "https://github.com/katilingban/washdata/"
	cran = "washdata" 

	version("0.1.3", md5="a048f2163a63f10a3eaf9c91d3d3d2c9")

	depends_on("r@2.10:", type=("build", "run"))
