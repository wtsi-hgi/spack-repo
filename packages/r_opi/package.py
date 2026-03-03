# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpi(RPackage):
	"""Open Perimetry Interface

	Implementation of the Open Perimetry Interface (OPI) for simulating and controlling visual field machines using R. The OPI is a standard for interfacing with visual field testing machines (perimeters) first started as an open source project with support of Haag-Streit in 2010. It specifies basic functions that allow many visual field tests to be constructed. As of February 2022 it is fully implemented on the Haag-Streit Octopus 900 with partial implementations on the Centervue Compass, Kowa AP 7000, Android phones and the CrewT IMO. It also has a cousin: the R package 'visualFields', which has tools for analysing and manipulating visual field data.
	"""
	
	homepage = "https://people.eng.unimelb.edu.au/aturpin/opi/index.html"
	cran = "OPI" 

	version("2.11.2", md5="3bbcdfd8763a6c39dc18214f73fe8c75")

	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
